# Gerrit Deploy

### gerrit.config

```sh
[gerrit]
    basePath = git
    canonicalWebUrl = http://xx.xx.xx.xx:8081
    serverId = fe37d9bb-1f83-4f35-9b68-56ffa056c02b
[container]
    javaOptions = "-Dflogger.backend_factory=com.google.common.flogger.backend.log4j.Log4jBackendFactory#getInstance"
    javaOptions = "-Dflogger.logging_context=com.google.gerrit.server.logging.LoggingContext#getInstance"
    user = root
    javaHome = /usr/lib/jvm/java-11-openjdk-11.0.15.0.10-2.el8_6.x86_64
    javaOptions = -Djava.security.egd=file:/dev/./urandom
    javaOptions = --add-opens java.base/java.net=ALL-UNNAMED
    javaOptions = --add-opens java.base/java.lang.invoke=ALL-UNNAMED
    javaOptions = -Djava.security.egd=file:/dev/./urandom
    javaOptions = --add-opens java.base/java.net=ALL-UNNAMED
    javaOptions = --add-opens java.base/java.lang.invoke=ALL-UNNAMED
    javaOptions = -Djava.security.egd=file:/dev/./urandom
    javaOptions = --add-opens java.base/java.net=ALL-UNNAMED
    javaOptions = --add-opens java.base/java.lang.invoke=ALL-UNNAMED
    javaOptions = -Djava.security.egd=file:/dev/./urandom
    javaOptions = --add-opens java.base/java.net=ALL-UNNAMED
    javaOptions = --add-opens java.base/java.lang.invoke=ALL-UNNAMED
    javaOptions = -Djava.security.egd=file:/dev/./urandom
    javaOptions = --add-opens java.base/java.net=ALL-UNNAMED
    javaOptions = --add-opens java.base/java.lang.invoke=ALL-UNNAMED
[index]
    type = lucene
[auth]
    type = ldap
    gitBasicAuthPolicy = HTTP
[receive]
    enableSignedPush = false
[sendemail]
    smtpServer = smtp.mxhichina.com
    smtpServerPort = 465
    smtpEncryption = SSL
    from = devops-cst@x-peng.cn
    smtpUser = devops-cst@x-peng.cn
    smtpPass = NHF#wqPV
[sshd]
    listenAddress = *:29418
[httpd]
    listenUrl = http://*:8080/
[cache]
    directory = cache
[plugins]
    allowRemoteAdmin = true
[plugin "avatars-gravatar"]
    type = identicon
```

### replication.config

```bash
[gerrit]
    autoReload = true
    replicateOnStartup = true
[replication]
    lockErrorMaxRetries = 5
    maxRetries = 5
[remote "gitlab"]
    url = xx.git
    push = +refs/heads/*:refs/heads/*
    push = +refs/tags/*:refs/tags/*
    threads = 3
    rescheduleDelay = 15
```

### docker-compose.yaml

```yaml
version: '3'
volumes:
  gerrit_plugins_vol:
services:
  gerrit:
    user: root
    image: gerrit:3.6.1
    ports:
      - "29418:29418"
      - "8081:8080"
    volumes:
      - gerrit_plugins:/var/gerrit/plugins
      - ./external/gerrit/etc:/var/gerrit/etc
      - ./external/gerrit/git:/var/gerrit/git
      - ./external/gerrit/db:/var/gerrit/db
      - ./external/gerrit/index:/var/gerrit/index
      - ./external/gerrit/cache:/var/gerrit/cache
      - ./external/gerrit/.ssh:/root/.ssh
    environment:
      - CANONICAL_WEB_URL=http://xx.xx.xx.xx:8081
    # command: init
```

```Plaintext
docker run -ti -p 8080:8080 -p 29418:29418 -v $(pwd)/etc:/var/gerrit/etc gerritcodereview/gerrit:3.5.4
```
