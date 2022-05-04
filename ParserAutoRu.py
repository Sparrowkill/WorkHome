import requests
from selenium import webdriver

import json
# driver = webdriver.Chrome()
# driver.get("https:/auto.ru")
#HTTP запрос
def fetch(url, params):
    headers = params ['headers']
    body = params['body']
    if params ['method']=='POST':
        return requests.post(url, headers=headers, data=body)
    else:
        return requests.get(url, headers=headers)


x = fetch("https://auto.ru/-/ajax/desktop/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"101\", \"Google Chrome\";v=\"101\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "25.0.9412765",
    "x-client-date": "1651662192584",
    "x-csrf-token": "32e2c583c5a48812f91b400c81494e4cf9065691771caf0a",
    "x-page-request-id": "29f74db667481f2146c6c5ed880c8f15",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/cars/vaz/all/on-credit/",
    "x-yafp": "{\"a1\":\"uc775kyzikk6ow==;0\",\"a2\":\"vEiudYFEY2uV7WH2/8Gat3ei66NWrQ==;1\",\"a3\":\"RsaP0vdGi9PHAaYeG6SZdg==;2\",\"a4\":\"sexl6Nte95TllnKZXevZorvefPgRlmXiptOqSYi5OOdKNg==;3\",\"a5\":\"CP7pjHWJAPhY6A==;4\",\"a6\":\"WfU=;5\",\"a7\":\"ZSC2XhgVBT67kA==;6\",\"a8\":\"MwZxvZrWSnk=;7\",\"a9\":\"QgiStB2dHiG0qQ==;8\",\"b1\":\"QDxGq27Agm4=;9\",\"b2\":\"MkKIh9YcVOdS/Q==;10\",\"b3\":\"bkAzsbrdsuYcIg==;11\",\"b4\":\"3Q4AuhlveDM=;12\",\"b5\":\"BzPI0wbhMwyqxQ==;13\",\"b6\":\"HUcGzwF93C4+tQ==;14\",\"b7\":\"98iXbubZEczgUw==;15\",\"b8\":\"C/mNWudoAX8wpQ==;16\",\"b9\":\"fjs7PH/qNYMlQQ==;17\",\"c1\":\"8RX8DQ==;18\",\"c2\":\"RAOuuPDNbU7MXZNpxNme7A==;19\",\"c3\":\"PEs071409soQkjfV0ntnrg==;20\",\"c4\":\"B90AL+N3wpo=;21\",\"c5\":\"axkhFIW58kA=;22\",\"c6\":\"DIMeRw==;23\",\"c7\":\"pRONfKt126U=;24\",\"c8\":\"B+0=;25\",\"c9\":\"np45ySa/6uw=;26\",\"d1\":\"CbrpnaQh9cM=;27\",\"d2\":\"Boo=;28\",\"d3\":\"JCiG5/OTwaPaWw==;29\",\"d4\":\"DDNkT6cI0d0=;30\",\"d5\":\"8UPYsfwEQu8=;31\",\"d7\":\"haYZp+GuFu8=;32\",\"d8\":\"ei2xVX5b8sRXZ9SUonps/Oz+NmfWjlz8ELI=;33\",\"d9\":\"fJKHyNJ43JM=;34\",\"e1\":\"viDwQMlMU/gy2w==;35\",\"e2\":\"FqBnCjCeojo=;36\",\"e3\":\"jL1ta+U1dUI=;37\",\"e4\":\"aJIIfatpYb4=;38\",\"e5\":\"qVY5ZZV9NjniPQ==;39\",\"e6\":\"mXsY1Nff4i0=;40\",\"e7\":\"VjjA/oJPUKH5+Q==;41\",\"e8\":\"kqdH3XjSafU=;42\",\"e9\":\"Qat5DNZ8y7U=;43\",\"f1\":\"gY5d/5Bjk4Qzdg==;44\",\"f2\":\"ck2m78v0M24=;45\",\"f3\":\"zBj2mYpK686hTQ==;46\",\"f4\":\"6lVeIIy3O5E=;47\",\"f5\":\"pgKcHj4q+fuyMw==;48\",\"f6\":\"HYeELUM516J4YQ==;49\",\"f7\":\"DWlbTGy1O+1yGg==;50\",\"f8\":\"pQWX9pGkbgCKYw==;51\",\"f9\":\"JmmcIQ0KOtk=;52\",\"g1\":\"TO+XQ5mMclE3ZQ==;53\",\"g2\":\"4YSxPrdIKYFEPQ==;54\",\"g3\":\"jbvXQ5n5OLE=;55\",\"g4\":\"lRhhspgKwIbtiQ==;56\",\"g5\":\"LExJFuW7DN8=;57\",\"g6\":\"GXT/zRcRTtU=;58\",\"g7\":\"cxU0l0ZYZ4U=;59\",\"g8\":\"XaZbWZDn1Jo=;60\",\"g9\":\"8to5IwT/iE4=;61\",\"h1\":\"hs2OmX4x1zS2sg==;62\",\"h2\":\"nKheDJVyCrZ+yg==;63\",\"h3\":\"A/o7MNtu2i2czQ==;64\",\"h4\":\"dqem/H1VLkxUMw==;65\",\"h5\":\"5hV2Tfdrp2o=;66\",\"h6\":\"ZPprGHQTknnz0Q==;67\",\"h7\":\"aj0M/Le8B67i0bA4YV7pueGM7oKtUZ1lout0SP3OuTUT50i6;68\",\"h8\":\"quo6cRq2aIPgcA==;69\",\"h9\":\"UoAI9lBMPveO9A==;70\",\"i1\":\"mhu8zavvMzU=;71\",\"i2\":\"0cfU7C3bFWBQ+Q==;72\",\"i3\":\"yLGji+W9gB3Oxg==;73\",\"i4\":\"B6HRtAdq+ngApA==;74\",\"i5\":\"DSrploxB05sw9w==;75\",\"z1\":\"CfgYBURjD9TlfgywAxB+00xvt3CbqeU+rbAO09sDD8+6GC7gMwV7Wt1jHFjn71er8Zib+/JX35a6R+EI0bI15g==;76\",\"z2\":\"9JwWfytfhKmHJzBN0mtEMMUFM5ql/Or7WSbDt7GVMnDCdf8/lZB4y/NjWW/vgWH/M0qvo0qG2Ay4xkNdc4i3aw==;77\",\"y2\":\"/Mfadiog46czWQ==;78\",\"y3\":\"dvN/6i7X4a6Ukg==;79\",\"y6\":\"AO4JtAiRzgmInA==;80\",\"y8\":\"OCiVex4LgagclQ==;81\",\"x4\":\"uPGEcrTqjK8LJA==;82\",\"z5\":\"TuBGBhZfaPA=;83\",\"z4\":\"8G34ZJqNwWrASQ==;84\",\"z6\":\"cQ6dTZB42mAOyYWJ;85\",\"z7\":\"+jWmiFK52/HMDNUJ;86\",\"z8\":\"29DaU20coFjuTJh579E=;87\",\"z9\":\"IwogmZtfeLyfVZ/h;88\",\"y1\":\"Feosfu9KtB2aKuMg;89\",\"y4\":\"+VsuOS5oz6x05sPp;90\",\"y5\":\"wenW371qvsT5viwAvM4=;91\",\"y7\":\"4ej2o9hAzJ2dw4BO;92\",\"y9\":\"sTmev2XuuOySeG5xmps=;93\",\"y10\":\"oSqGuZabPFIMH/Ow+ec=;94\",\"x1\":\"NXB4hYdLtG1VVsJy;95\",\"x2\":\"x+e69lhrjywuz1oDJK0=;96\",\"x3\":\"g3Y6ZNpN7btMstMo;97\",\"x5\":\"4lz/TaAfPHydi5MH;98\",\"z3\":\"XtrLClOnfJ5qn4IVbV2Cm3jl5LfYOjJF3rRPpAt4Vpg=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"Iz1u3JqE9y9n9YzU73P3iyHqxLA=;100\",\"pgrd\":\"6ypzqf0aTwPjVA7GNvMHHzhgGfIFWD3Z8CF37pcCND5hTxGeQ+UUTAL2KjLYT1SiYshEd+agGTurRH4s5H+Xq4OAHPrqwEOv7n7tLZg7hO6uDIudKezQIqGUFRKrjaVTsWtJ8g0vJcf0XgxncX8SQ54JNag/UnxwLoLrkuqpPmBZpOLRCk+C1ypiznNq6iQgqQPCjaUajm5Je3W6/LxowPpgIZM=\"}",
    "cookie": "autoru_sid=a%3Ag62724e9427bjum713ph43nntvil590f.83b000c324389edc9272ef1bbdc49e23%7C1651658388110.604800.YhK5pXnDrAAq3PTxrd7NRw.AWJv0kJX4rcbnB-COn3s6fySSna0uEGLR2UhB2mn8J8; autoruuid=g62724e9427bjum713ph43nntvil590f.83b000c324389edc9272ef1bbdc49e23; autoru_gdpr=1; suid=0775605e2e1cfe2ee67060a165841a59.7be6a6150cef3afd511e744bfd8fbb8f; yuidlt=1; yandexuid=9241250471651658376; ys=searchextchrome.Commertial%23; crookie=8aUE88M1GsMIFBylNjFPXqmwhcYW2IN6zox3LbU2fameWsNYwFcX7FO3yxDxwg47/lP/DXby4zsXjMNekSOrx/+ajfY=; cmtchd=MTY1MTY1ODQwNTA3Nw==; _csrf_token=32e2c583c5a48812f91b400c81494e4cf9065691771caf0a; from=direct; Session_id=noauth:1651659199; yandex_login=; i=PVJLr2KIkr4eVKBUBd6bF+XRn0hqs3fxqOk9NbhStVcn5thxSzuHw7mv/lDFWz+aOHks/XYU/jSZo++TG6c3s7hhtVA=; mda2_beacon=1651659199983; sso_status=sso.passport.yandex.ru:blocked; gdpr=0; _ym_isad=2; _ym_uid=1651659222646125522; cycada=l0yV+514C6C0dZQxDUtAOU6oqkqGKJEx/081S0RtSss=; _yasc=JAMSBnSbOYnwJkk2FYtMiFc4W57xAYlEahcjmAsQ8eUU0M0V; from_lifetime=1651662171452; _ym_d=1651662171",
    "Referer": "https://auto.ru/cars/vaz/all/on-credit/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"catalog_filter\":[{\"mark\":\"VAZ\"}],\"on_credit\":true,\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\"}",
  "method": "POST"
})

print(x)

result = x.json()

# print(result)
# print (result.keys())
# print(result['offers'][0]['state']['mileage'])
USD1 = (result['offers'][0]['state']['mileage'])
print(type(USD1))
vazs = result['offers']
for vaz in vazs:
    print(f"модель {vaz['vehicle_info']['model_info']['name']} meleage: {vaz ['state']['mileage']}, USD {vaz['price_info']['USD']}")
   


   





