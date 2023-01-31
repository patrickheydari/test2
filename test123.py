for x in productsfullcol.find():

    dictsend={}
    if "title" in x:
        dictsend['title']=x['title']
    if "asin" in x:
        dictsend['asin']=x['asin']
        dictsend['url']="https://www.amazon.com/dp/"+str(x['asin'])    if "upcList" in x:
        dictsend['upcList']=x['upcList']
    if "eanList" in x:
        dictsend['eanList']=x['eanList']
    if "upc" in x:
        dictsend['upc']=x['upc']    if "brand" in x:
        dictsend['brand']=x['brand']    if "partNumber" in x:
        dictsend['partNumber']=x['partNumber']    x = producturlscol.insert_one(dictsend)