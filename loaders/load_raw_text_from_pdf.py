from langchain_community.document_loaders import PyPDFLoader


def load_raw_text_from_pdf(path: str, filename: str): 
    full_text = ""
    try:            
        loader = PyPDFLoader(path)
        pages = loader.load()

        full_text = " "+"\n".join([p.page_content for p in pages])
    except Exception as e:
            print(f"Skipped {filename}: {str(e)}")
            
    return full_text