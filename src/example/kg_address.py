def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    def _gettext(list):
        if not list:
            return list
        else:
            return list[0].strip()


    def clean_dict(items):
        result = {}
        for key, value in items.items():
            if value is None or value == '' or value == []:
                value = '---'
                result[key] = value
            else:
                result[key] = items[key]
        return result

    def get_next_url(url):
        spl_1 = url.split("page=")
        spl_2 = spl_1[1].split("&")
        num = int(spl_2[0])+1
        return spl_1[0]+"page="+num+"&"+spl_2[1]


    for i in range(1,len(page.xpath('//tbody/tr'))+1):
        address_id = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[2]//text()"))
        list_street_ky = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[3]/div[@class='list-street']/p//text()"))
        street_type_ky = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[3]/div[@class='street-type']/span//text()"))
        list_street_ru= _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[4]/div[@class='list-street']/p//text()"))
        street_type_ru= _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[4]/div[@class='street-type']/span//text()"))
        pr_list_street_ky = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[5]/div[@class='list-street']/p/text()"))
        pr_street_type_ky = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[5]/div[@class='street-type']/span//text()"))
        pr_list_street_ru = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[6]/div[@class='list-street']/p/text()"))
        pr_street_type_ru = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[6]/div[@class='street-type']/span//text()"))
        orig_addr = _gettext(page.xpath("//tbody/tr["+str(i)+"]/td[7]//text()"))
        
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
        "pr_street_type_ru":pr_street_type_ru,  
        "orig_addr":orig_addr

        }

        url_dict = {
            'url': get_next_url(url)
        }

        print(url)
        print(get_next_url(url))
        context.emit(rule = "store", data = clean_dict(org_data))

        print("----------------Printing Org Data------------------")
        print(org_data)

    context.emit(rule = "fetch", data = url_dict)

