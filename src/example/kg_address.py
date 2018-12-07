def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html



for i in range(len(page.xpath("//tbody/tr/td[@class='center'][2]//text()"))):
    address_id = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[2]//text()"))
    list_street_ky = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[3]/div[@class='list-street']/p//text()"))
    street_type_ky = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[3]/div[@class='street-type']/span//text()"))
    list_street_ru= _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[4]/div[@class='list-street']/p//text()"))
    street_type_ru= _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[4]/div[@class='street-type']/span//text()"))
    pr_list_street_ky = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[5]/div[@class='list-street']/p/text()"))
    pr_street_type_ky = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[5]/div[@class='street-type']/span//text()"))
    pr_list_street_ru = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[6]/div[@class='list-street']/p/text()"))
    pr_street_type_ru = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[6]/div[@class='street-type']/span//text()"))

   

org_data = {
"url": response.url,
"address_id": address_id,
"list_street_ky":list_street_ky,
"street_type_ky":street_type_ky,
"list_street_ru":list_street_ru,
"street_type_ru":street_type_ru,
"pr_list_street_ky":pr_list_street_ky,
"pr_street_type_ky":pr_street_type_ky,
"pr_list_street_ru":pr_list_street_ru,
"pr_street_type_ru":pr_street_type_ru

}

print("----------------Printing Org Data------------------")
print(org_data)

context.emit(data=org_data)

    

def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()