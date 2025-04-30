import requests
from bs4 import BeautifulSoup

def fetch_pubmed_articles_with_metadata(query : str,max_results=3,use_mock_if_empty=True):
    headers={"User-Agent":"Mozilla/5.0"}

    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results,
    }
    try:
        search_response = requests.get(search_url, headers=headers, params=search_params,timeout=10).json()
        id_list=search_response["esearchresult"]["idlist"]
        print(" Found PubMed IDs: ",id_list)
        if not id_list:
            raise ValueError("No IDs found for this query")
        
        ids=','.join(id_list)

        fetch_url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        fetch_params={
            "db":"pubmed",
            "id":ids,
            "retmode":"xml"
        }

        fetch_response=requests.get(fetch_url,headers=headers,params=fetch_params,timeout=10)
        soup=BeautifulSoup(fetch_response.content,"lxml")
        articles_xml=soup.find_all("PubmedArticle")
        print("Articles found in XML : ",len(articles_xml))

        articles_info=[]
        for article,pmid in zip(articles_xml,id_list):
            title_tag=article.find("articletitle")
            abstract_tag=article.find("abstract")
            date_tag=article.find("pubdate")
            author_tags=article.find_all("author")

            title=title_tag.get_text(strip=True)if title_tag else "No title found"

            abstract=abstract_tag.get_text(separator=" ",strip=True)if abstract_tag else "No abstract found"

            authors=[]
            for author in author_tags:
                last=author.find("lastname")
                fore=author.find("forename")
                if last and fore:
                    authors.append(f"{fore.get_text()} {last.get_text()}")
                elif last:
                    authors.append(last.get_text())

            authors=authors if authors else ["No authors listed"]

            pub_date="No date"
            if date_tag:
                year=date_tag.find("year")
                month=date_tag.find("month")
                pub_date=f"{month.get_text()} {year.get_text()}" if year and month else year.get_text() if year else "No Date"

            url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"

            print(f" Article : {title}\n - Authors:{authors}\n - Date : {pub_date}\n - URL: {url}\n")
            articles_info.append({
                "title":title,
                "abstract":abstract,
                "authors":authors,
                "publication_date":pub_date,
                "article_url":url
            })
        
        if not articles_info and use_mock_if_empty:
            print("No valid articles found, returning mock data.")
            return[{
                "title":"Simulated Study on Fever",
                "abstract":"This is a simulated abstract on the treatment of fever in adults",
                "authors":["Pradeesh","Vishal","vishnu","ooga"],
                "publication_date":"May 2025",
                "article_url":"https://github.com/your-medical-project"
            }]
        return articles_info
    
    except Exception as e:
        print(f" Error during pubmed fetch: {e}")
        if use_mock_if_empty:
            return [{
                "title":"Simulated study on fever",
                "abstract":"This is a simulated abstract on the treatment of fever in adults",
                "authors":["Pradeesh","Vishal","vishnu","ooga"],
                "publication_date":"May 2025",
                "article_url":"https://github.com/your-medical-project"
            }]
        else:
            return [{"message": f"Error : {e}"}]