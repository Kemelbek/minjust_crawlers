    def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html


  
    name_ru = _gettext(page.xpath("//span[contains(text(),'2. П')]/../../following-sibling::td//text()"))
   

    org_data = {
    "url": response.url,
    
    "name_ru": name_ru,
    
    }

    print("----------------Printing Org Data------------------")
    print(org_data)

    context.emit(data=org_data)

    

def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()
