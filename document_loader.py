import os
import re
from typing import List, Dict, Any
from pathlib import Path


def extract_metadata_from_frontmatter(content: str) -> Dict[str, Any]:
    """Extract YAML frontmatter metadata from markdown content."""
    metadata = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            for line in frontmatter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
    return metadata


def clean_markdown_content(content: str) -> str:
    """Clean markdown content by removing frontmatter and excessive whitespace."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2]
    
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    
    return content.strip()


def load_markdown_documents(knowledge_base_path: str = "knowledge_base/cloudru") -> List[Dict[str, Any]]:
    """Load all markdown documents from the knowledge base directory."""
    documents = []
    base_path = Path(knowledge_base_path)
    
    if not base_path.exists():
        return documents
    
    for md_file in base_path.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata = extract_metadata_from_frontmatter(content)
            cleaned_content = clean_markdown_content(content)
            
            relative_path = md_file.relative_to(base_path)
            topic = md_file.parent.name if md_file.parent != base_path else "general"
            
            doc = {
                "content": cleaned_content,
                "metadata": {
                    "source": str(relative_path),
                    "file_name": md_file.name,
                    "topic": metadata.get("topic", topic),
                    "title": metadata.get("title", md_file.stem.replace("_", " ").replace("-", " ").title()),
                    "url": metadata.get("url", ""),
                    "source_name": metadata.get("source", "Cloud.ru Documentation")
                }
            }
            documents.append(doc)
        except Exception as e:
            print(f"Error loading {md_file}: {e}")
            continue
    
    return documents


def chunk_document(doc: Dict[str, Any], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Dict[str, Any]]:
    """Split a document into smaller chunks for better retrieval."""
    content = doc["content"]
    metadata = doc["metadata"]
    chunks = []
    
    sections = re.split(r'\n##\s+', content)
    
    current_chunk = ""
    current_section = ""
    
    for i, section in enumerate(sections):
        if i > 0:
            section = "## " + section
        
        section_title_match = re.match(r'^##?\s+(.+?)$', section, re.MULTILINE)
        if section_title_match:
            current_section = section_title_match.group(1)
        
        paragraphs = section.split('\n\n')
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
                
            if len(current_chunk) + len(para) <= chunk_size:
                current_chunk += para + "\n\n"
            else:
                if current_chunk.strip():
                    chunk_metadata = metadata.copy()
                    chunk_metadata["section"] = current_section
                    chunks.append({
                        "content": current_chunk.strip(),
                        "metadata": chunk_metadata
                    })
                
                if len(para) > chunk_size:
                    words = para.split()
                    temp_chunk = ""
                    for word in words:
                        if len(temp_chunk) + len(word) + 1 <= chunk_size:
                            temp_chunk += word + " "
                        else:
                            if temp_chunk.strip():
                                chunk_metadata = metadata.copy()
                                chunk_metadata["section"] = current_section
                                chunks.append({
                                    "content": temp_chunk.strip(),
                                    "metadata": chunk_metadata
                                })
                            temp_chunk = word + " "
                    current_chunk = temp_chunk
                else:
                    overlap_text = current_chunk[-chunk_overlap:] if len(current_chunk) > chunk_overlap else ""
                    current_chunk = overlap_text + para + "\n\n"
    
    if current_chunk.strip():
        chunk_metadata = metadata.copy()
        chunk_metadata["section"] = current_section
        chunks.append({
            "content": current_chunk.strip(),
            "metadata": chunk_metadata
        })
    
    return chunks


def prepare_documents_for_indexing(knowledge_base_path: str = "knowledge_base/cloudru") -> List[Dict[str, Any]]:
    """Load and chunk all documents for indexing."""
    documents = load_markdown_documents(knowledge_base_path)
    all_chunks = []
    
    for doc in documents:
        chunks = chunk_document(doc)
        all_chunks.extend(chunks)
    
    print(f"Loaded {len(documents)} documents, created {len(all_chunks)} chunks")
    return all_chunks
