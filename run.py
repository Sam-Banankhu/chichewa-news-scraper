from assets.functions import *

base_url = 'https://www.radiomaria.mw/news/'
for i in tqdm(range(1, 228), desc='Progress', unit='#', ncols=80):
    try:
        if i == 1:
            url = base_url
        else:
            url = f'{base_url}page/{str(i)}/'
            
        s = get_url(url)
        titles, news, links, date, author = get_links_title(s)
        print(len(titles), len(news), len(links), len(date), len(author))
        df = create_csv(titles, news, links, date, author)
    except Exception as e:
        # Print the error message or handle it as needed
        print(f"An error occurred at iteration {i}: {str(e)}")
        continue


df.to_csv("final_radio_maria_chichewa_lang_news.csv",index = False)