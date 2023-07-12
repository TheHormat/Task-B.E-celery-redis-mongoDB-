
## Problems

1. Dockerde project qaldırılır amma collectstatic etməmə rəğmən css kodları gəlmir.

2. İp adresi ilə yoxlama və 5 saat sonra silinməsi. Kod olaraq doğru yazdığımı düşünürəm amma yüklənən paketlərin versiyasına əsasən kodun tam çalışmasında sıxıntlar olur.

## Those used on the technical side

*Django / PostgreSql / MongoDB / Docker / Celery / Redis*


  
## API Usage

#### Fetch all items

```http
  GET /api/users
```
Bu url ilə biz bütün dataları görür, həmin url-də POST ilə yeni data əlavə edə bilirik


#### Fetch item

```http
  GET /api/users/${id}
```
Burada mövcud data haqqında daha geniş məlumat alırıq. PUT metodu ilə update edə və yeniliyə, DELETE metodu ilə user-i silə bilirik.

#### Fetch IP address

```http
  GET /api/ipwhitelist
```

Bu url-də GET ilə İP address-lərini görə, POST metodu ilə yeni bir İP addresi əlavə edə bilirik.



  
## Appendices

NoSQL olaraq MongoDB-dən istifadə olunub.Proyekt PostgreSql databazasından istifadə edilərək qaldırılır.Celery və Redis tam şəkildə qoşularaq çalışır.Docker-compose up edərək proyekt servərə qaldırılır. Nginx ayarlarında istifadə elədiyim bəzi ayarlamalar DigitialOceanda yaratdığım droplet-ə məxsusdur.

Kod olaraq doğru yazdığımı düşünürəm, shell-də yoxladıqdada istədiyim nəticəni alıram sadəcə tam vaxt edib paketlərlə bağlı sıxıntıya baxa bilmədim.

  
