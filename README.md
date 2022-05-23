<!-- ex_nonav -->
# [notebook](https://fanxiangs.github.io/notebook/)

## git book
### build book

```shell
export gitbookImage=gitbook
#  Generate a `SUMMARY.md`
docker run --rm -v "$PWD:/srv/gitbook" -p 4000:4000 ${gitbookImage} book sm
# install plugin
docker run --rm -v "$PWD:/srv/gitbook" -p 4000:4000 ${gitbookImage} gitbook install
# run serve or build
docker run --rm -v "$PWD:/srv/gitbook" -p 4000:4000 ${gitbookImage} gitbook serve
```
### build gitbook image
```shell
# build
docker build -t gitbook .
# pull
docker pull fanxiangs/gitbook
```