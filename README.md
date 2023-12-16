# zzuli_gplt

如有任何问题，都可以直接提出 issuse 与 pr。

## 软件前置要求

云上服务器需要开通相应的端口号，在安全组上进行开通，80，3306，443基本默认开通，`请一定要开通3000端口号`。

在linux平台上需要的前置软件需要，这里使用的是 xshell连接数据库进行平台部署，然后navicat连接数据库进行修改信息，docker在linux上运行，然后将将项目运行起来

`注意:项目会默认占用80，3306，443，3000端口，如果端口被占用，应先停下其被占用的端口的程序,暂停例子如下`：

```shell
sudo systemctl stop apache2.service # 暂停apache2
sudo systemctl stop mysql.service # 暂停mysql
ps -ef | grep nginx
kill -9 xxxx # nginx 查到的PID端口号
```

如果想换占用的端口，请修改`backend/docker-compose.yml`里面的内容，（有注释，请自行修改相关端口号）

### windwos

因为`nodejs`版本错综杂乱，前端的构建建议在windwos平台上进行构建，

软件需要：

- nodejs 20.04 （直接在官网上下载lts版本就行了）
- xshell (ssh连接linux使用)
- navicat (连接数据库使用)

### linux

以ubuntu版本为例，如果是其他版本，换一下包管理器就可以了

```shell
sudo apt install docker-ce # 每一个发行版是不一样的
sudo systemctl start docker.service # 启动 docker
# 每一个版本是不一样的，下面部署的时候可以根据报错信息来安装对应的软件
sudo apt install docker-compose # 运行 docker 使用的
sudo apt install lrzsz # xshell 进行传输文件
```

## 项目大致结构

- `zzuli-vue`是前端，需要发送api请求到后端，所以如果要部署项目的话，那么就需要修改前端的api请求
- `zzuli-rank`是后端，是所有的文件，默认生成的dist文件已经在此里面了，但是每次配置的ip地址不同，需要根据需要构建前端，然后放到`backend/fronted/html/`里面即可。
- `template`是模板，导入到数据库里面去的。

以下是部署此项目的大致流程

### 前端

前端需要修改`api`请求地址，并且使用`nodejs`进行编译生成目标文件`dist`,并且放入到`backend/frontend/html`文件中即可。

修改的地址是`zzuli-vue/config.js`中，将其中的ip地址改成对应服务器的ip地址即可

以上文件都有相关注释，根据注释进行改动。

然后进行编译（一下操作建议在windwos平台上进行，非常快就可以build生成）：

```shell
npm install # 下载相关插件
npm run build # 生成 dist文件
```

dist文件即是目标文件，放入到`backend/frontend/html/dist`里覆盖dist文件即可。

### 后端

后端基本不需要进行修改，如果需要修改，那么是此文件

- backend/docker-compose.yml

此文件已经写好了注释，根据注释进行修改。

### docker，启动

docker一开始启动的时候，需要拉去镜像文件，所以比较慢，耐心等待即可

```shell
docker-compose up -d # docker,启动！
# ing ... 服务就开始正常运行了，
```

如果需要停止

```shell
docker-compose down
```

即可。

### 数据库

使用`navicat`连接数据库，`需要将数据导入到数据库PTA_Data`中，默认配置如下

```text
user: root
password: zzulirank_2023
```

使用以上账号即可登录数据库，然后`需要根据excel表格导入到数据库里面，只需要处理两个表即可： Student_Info 和 Team_Info`即可，`这里我们选择使用excel表格进行导入`。

模板在：`zzuli_gplt/template`里面，有一份excel表格，里面有两个sheet,根据模板的样子填写即可，然后导入到数据里面即可

`注意：这里id要保证唯一，并且数据一定要对，否贼后台算分数的时候会错误`,`并且teamID一定要对应`,以下是例子

- 队伍清单

```text
TeamID   TeamName               Class
231001    莫比乌斯反演队友      计算机科学与技术xx-xx班级
```

- 成员清单

```text
team_id team          class             stuid            name
231001 莫比乌斯反演队友 计算机科学与技术 542xxxxxxxxx 王小明
231001 莫比乌斯反演队友 计算机科学与技术 542xxxxxxxxx 小王
```

`注意team_id一定要对其，并且要唯一`

## 管理界面

管理界面默认即使`(http://localhost/zzulirank_manage`，这里面填写对应的`PTA_Session`和`Problem_Set`即可，并且修改分数也可以的,注意，这里将名字写上去，前台就可以显示出对应的榜单的名字了

>`PTA_Session`和`Problem_Set`通过是本次比赛cookie相关，向老师询问或者自己检查，就可以得到相关`cookie`。

此时，榜单就可以进行运作了

## 结束之后

### 开启关闭相关服务

docker-compose可以进行相应的数据管理，

```text
前端服务名：zzulirank-frontend
后端服务名：zzulirank-backend
爬虫脚本服务名：zzulirank-data_updater
数据库服务名：zzulirank-mysql
```

```shell
# 开启相关的服务名
docker-compose unpause xxxxx # xxx 上面的服务名
# 关闭相关的服务器名
docker-compos pause xxxx
```

比赛结束之后，就可以停止爬虫脚本的工作了，只让其他的工作，供别人展示。

### 重新开启一个新的榜单

只要将数据库中的表格导入成新的数据库，然后再榜单页面中重新设置新的`Session`和`Problem_set`即可生成新的榜单。
