[toc]
[git教程](https://www.liaoxuefeng.com/wiki/896043488029600)
#	基础Git命令操作
##  2.1拉取分支
进入项目目录，运行git pull保证当前项目是最新master版本，通过git branch可查看当前处于哪个分支。然后运行git checkout -b new_branch_name创建新分支。
$ cd demo （项目目录）
$ git pull (更新代码)
$ git branch (查看分支)
$ git checkout -b new_branch (从当前分支拉取新分支，此处是本地分支)

##  2.2	在新分支上开发并提交到远端分支上
在新分支上进行修改、开发完成后，可以用git status命令确定修改文件当前处于什么状态（哪些文件需要git add，哪些文件需要git commit）；用git add命令跟踪修改的文件；用git commit命令提交更新到本地仓库分支上；然后用git push命令将更新推送到远端仓库分支上。
$ git status
$ git add file 或者 git add .
  (变为stage状态，被git管理，通过git reset HEAD .回到unstage状态)
$ git commit -m 'update message'
$ git push origin new_branch 
（push之前可先执行git pull --rebase把远端分支最新代码同步到本地，对于多人协同开发一个分支比较好用,出现冲突解决参考后面章节）
查看修改历史记录的是git log，不是git status
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191108143257698.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzMDg2MTA2,size_16,color_FFFFFF,t_70)

##  2.3	分支合并到远端master
本地分支代码修改好之后，经过2.2节操作可以上传到远端仓库的分支上，最后要把远端分支上的代码Merge到远端master上，在codeclub上创建一个Merge Request。创建merge request的时候需要关联问题单
##  2.4	把master上最新代码同步到自己分支上
git checkout master
git pull （更新本地master）
git checkout 本地分支名
git fetch origin master
git rebase origin/master
然后git push到远端分支
后续在分支上继续开发，提交代码同前面2.2、2.3节操作。
百度上查了下理解为，git fetch origin master会在本地仓库创建一个master的副本，名字就是origin/master，然后git rebase origin/master这条命令就是这个master副本跟当前分支合并
##  2.5	Git命令查看本地/远程分支
git branch -l:查看本地分支
git branch -r:查看远程分支
git branch -a :查看全部分支（远程的和本地的）

##  2.6	本地创建分支之后，codeclub上看不到！
解决：
在git bash里面创建的分支，一定要经过push才能同步到远端服务器上，在codeclub上才能看到
##  2.7	误删了本地分支目录下的文件夹或文件，怎么恢复！
第一种：细致操作
先用git status查看下是哪个目录和文件被删除
然后用git checkout 目录/*.*   或git checkout 文件名
第二种：粗犷操作
直接git checkout 
##  2.8	删除远端分支
git push origin --delete yyc_test
##  2.9	删除本地分支
git branch -D 分支名
##  2.10	CodeClub之间切换project
Git bash打开本地master
git pull最新的master代码
git remote set-url origin ssh://ubp@**:2222/pshGITpublic/eAPP610.git
即可切换到新的鼎桥codeclub服务器上
可以用 git remote -v 查看是否切换对了
##  2.11	Git恢复之前版本的两种方法reset、revert（图文详解）
来自https://blog.csdn.net/yxlshk/article/details/79944535
##  2.12	Git证书问题，提示certificate signed authority error
从git上clone代码之后，push的时候如果出现下面问题，是本地git证书有问题
解决方法：
windows请按照下面链接中的第二种方法修复https://code.huawei.com/codeclub/support/issues/287
把附件的证书文件ca-bundle.crt 中的内容追加到本地证书文件后面
##  2.15	Push代码时自动merge：
Push代码的时候，如果远端分支上有最近的更新是本地分支上没有的，需要将远端分支上最新的代码更新到本地。这是git对合入时序性的要求，必须遵循。
简单的情况，需要merge，但是没有冲突，即填写自动merge的注释即可，会自动进行merge。
##  2.16	冲突产生的原因：
Git合入有时序性，即提交到远程中心仓库的代码必须是按照时间顺序的

###  2.16.1	冲突产生
1、master与分支冲突
在master分支，修改a.cpp为：
提交到服务器上。
在dev_test分支，修改a.cpp为
提交到服务器上。
如果此时两个分支合并，Git就无法"快速合并"了，就会生成冲突。当通过命令行merge时，会有如下提示。如果通过工具合并也会有冲突提示，此时就需要人工介入解决冲突了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191108143934533.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzMDg2MTA2,size_16,color_FFFFFF,t_70)
2，本地分支与远端分支冲突
这种一般出现在多人在同一个分支上协作开发的场景。
比如张三从远端仓库拿到代码后，对文件b.cpp进行了修改。然后push到远端仓库。
李四在张三之前就拿到了中心仓库的代码，在张三push成功之后也对b.cpp文件进行了修改。这个时候李四也运行push命令推送代码。此时就会提示冲突。
需要人工介入解决冲突了。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191108143956846.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzMDg2MTA2,size_16,color_FFFFFF,t_70)
###  2.16.2	冲突解决
1，手工解决冲突方法1
在文本编辑器或IDE里打开这个文件，就会看到这样的文件内容：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191108144048860.png)

Git用>>>>>>标记出不同分支的内容，上面HEAD表示当前分支的代码，下面的master表示master分支的代码。此时我们需要确认需要留哪部分的代码或者需要合并后的结果，那么一定要手动处理完再提交，将不需要的部分删掉，切记！
需要合并后的结果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191108144126132.png)
手动解决冲突方法2
建议本地下载一份完整的master代码或远端库上分支代码，与本地分支做BCompare用
发生冲突时，更新最新的master或远端库上分支代码，与本地分支作比较。
1）如果是不需要逻辑处理的冲突，只需将自己的修改部分按照方法1中的方式与库上代码merge即可。
2）如果冲突的代码需要做逻辑处理，例如需要添加分支处理等，则需要把本地修改先做另存，将库上代码重新pull，再将另存的代码合入。以确保库上冲突代码先下拉至本地分支，再合入自己的代码，即维持git合入的时序性。

解决完冲突后，再按照之前提交的步骤，git add ，git commit，git push提交到服务器就可以了。
在codeclub上的merge request不需要重新提交，在git push之后会重新启动编译。
###  2.16.3	执行git pull –rebase的必要性及冲突解决
在有些资料中看到git pull –rebase看这个命令，都说很神奇。这里推荐大家尝试使用。在git push之前执行git pull –rebase，经远端分支上的最新代码同步到本地
git pull --rebase = git fetch + git rebase
如果出现冲突，需采用2.16.2节中的解决方法。并且在解决冲突之后，用git add命令去更新这些内容，然后不用执行git-commit,直接执行git rebase --continue,这样git会继续apply余下的补丁。
在任何时候，都可以用git rebase --abort参数来终止rebase的行动，并且分支会回到rebase开始前的状态。
