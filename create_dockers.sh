#!/bin/bash

# для подключения к работающему контейнеру в другом терминале
# docker exec -it flow_container /bin/bash
# docker exec -it view_container /bin/bash
# docker exec -it base_container /bin/bash

# Или для присоединения к работающему в фоновом режиме
# docker attach flow_container
# docker attach view_container
# docker attach base_container

#!/bin/bash

# Сборка контейнеров
docker build -t cont_flow ./dock_flow
docker build -t cont_view ./dock_view
docker build -t cont_base ./dock_base

# Создание сети
docker network create dockers_network

# Запуск контейнера base_container
docker run -d --rm --network dockers_network -v "$(pwd)/dock_base/shared_folder:/app:Z" -v "$(pwd)/common_shared_folder:/common:Z" --name base_container cont_base

sleep 2

# Запуск контейнера flow_container
docker run -d -it --rm --network dockers_network -v "$(pwd)/dock_flow/shared_folder:/app:Z" -v "$(pwd)/common_shared_folder:/common:Z" --name flow_container cont_flow

sleep 2

# Запуск контейнера view_container
docker run -d -it --rm --network dockers_network -v "$(pwd)/dock_view/shared_folder:/app:Z" -v "$(pwd)/common_shared_folder:/common:Z" --name view_container cont_view

# Небольшая пауза для запуска контейнеров
sleep 2

# работа и вывод логов с разделителем
docker logs -f base_container &
docker logs -f flow_container &
docker logs -f view_container &

# Ожидание завершения view_container
docker wait view_container

# Остановка и удаление контейнеров
docker stop base_container flow_container
kill $(jobs -p)



    
