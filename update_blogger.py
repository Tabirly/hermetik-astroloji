import os
import pickle
from googleapiclient.discovery import build

def main():
    blog_id = "2621008100567662305"
    token_path = r"C:\Users\User\.gemini\antigravity\scratch\blogger_seo_sync\token.pickle"
    
    # Load OAuth token
    if not os.path.exists(token_path):
        print(f"HATA: Token dosyası bulunamadı: {token_path}")
        return
        
    with open(token_path, 'rb') as token:
        creds = pickle.load(token)
        
    service = build('blogger', 'v3', credentials=creds)
    
    # Read the updated HTML file
    html_path = "Sabian_Araci.html"
    if not os.path.exists(html_path):
        print("HATA: Sabian_Araci.html bulunamadı. Lütfen önce build_html.py çalıştırın.")
        return
        
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("Blogger sayfaları taranıyor...")
    request = service.pages().list(blogId=blog_id, fetchBodies=False, maxResults=500)
    response = request.execute()
    
    pages = response.get('items', [])
    target_page = None
    
    for page in pages:
        if "hermetik-astroloji-sembolleri" in page.get('url', ''):
            target_page = page
            break
            
    if not target_page:
        print("HATA: 'hermetik-astroloji-sembolleri' URL'sine sahip sayfa bulunamadı!")
        return
        
    print(f"Sayfa bulundu: {target_page['title']} (ID: {target_page['id']})")
    
    # Update the page
    print("Sayfa güncelleniyor...")
    update_body = {
        "content": html_content
    }
    
    update_request = service.pages().patch(
        blogId=blog_id, 
        pageId=target_page['id'], 
        body=update_body
    )
    
    update_response = update_request.execute()
    print("=======================================")
    print(f"BAŞARILI: '{update_response['title']}' sayfası canlı olarak güncellendi!")
    print(f"Canlı URL: {update_response['url']}")
    print("=======================================")

if __name__ == '__main__':
    main()
