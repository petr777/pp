# test 

## task 1
* SQL :
    ```
    SELECT clients.id, CONCAT(clients.first_name, ' ', clients.last_name), GROUP_CONCAT(DISTINCT category),  GROUP_CONCAT(product)
    FROM client_orders
    JOIN clients ON client_orders.client_id = clients.id
    JOIN orders  ON client_orders.order_id = orders.id
    WHERE age BETWEEN 18 and 65
    GROUP BY client_id
    HAVING COUNT(client_id) = 2 AND COUNT(DISTINCT category) = 1;
    ```

## task 2

* Git :
    ```
    https://github.com/petr777/pp.git
    cd pp
    ```
  
* Docker 
    ```
    docker-compose up --build
    ```

* You can use
  
  * [http://localhost:8080/api/v1?method=posts&profile=olgabuzova&limit=10](http://localhost:8080/api/v1?method=posts&profile=olgabuzova&limit=10)
  * [http://localhost:8080/api/v1?method=likes&link=https://m.vk.com/wall32707600_1203538](http://localhost:8080/api/v1?method=likes&link=https://m.vk.com/wall32707600_1203538)
  * [http://localhost:8080/api/v1?method=profile&profile=olgabuzova](http://localhost:8080/api/v1?method=profile&profile=olgabuzova)

  * [http://localhost:8080/api/v1?method=posts&profile=wylsa&limit=20](http://localhost:8080/api/v1?method=posts&profile=wylsa&limit=20)
  * [http://localhost:8080/api/v1?method=likes&link=https://m.vk.com/wall3460930_218134](http://localhost:8080/api/v1?method=likes&link=https://m.vk.com/wall3460930_218134)
  * [http://localhost:8080/api/v1?method=profile&profile=wylsa](http://localhost:8080/api/v1?method=profile&profile=wylsa)