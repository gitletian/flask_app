# babel
    1、首先让我们创建一个Babel的配置文件，文件名任意，这里我们取名为 babel.cfg 的 翻译配置文件
        这个文件告诉”pybabel”要从当前目录及其子目录下所有的”*.py”文件，
        和templates目录及其子目录下所有的”*.html”文件里面搜寻可翻译的文字，
        即所有调用”gettext()”，”ngettext()”和”_()”方法时传入的字符串。
        同时它告诉”pybabel”，当前Jinja2模板启用了autoescape和with扩展。

    2、接下来，在当前目录下，生成一个名为”messages.pot”的翻译文件模板
        pybabel extract -F babel.cfg -o messages.pot .
        参数”-F”指定了Babel配置文件；”-o”指定了输出文件名; "." 代表当前目录, 为必须参数。
        打开”messages.pot”，你会发现，上例中”No users”, “Test Sample”等文字都出现在”msgid”项中了。

    3、如果你在程序中用到了”lazy_gettext()”方法，那么你需要加上参数”-k lazy_gettext”来提醒pybabel要搜索该方法的调用：
       pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .

    4、首先记得将”messages.pot”中的”#, fuzzy”注释去掉，有这个注释在，将无法编译po文件。然后修改里面的项目信息内容如作者，版本等。
       创建”.po”翻译文件
       pybabel init -i messages.pot -d ./app/translations -l zh
       参数”-i”指定了翻译文件模板；”-d”指定了翻译文件存放的子目录，上例中我们放在”translations”子目录下；”-l”指定了翻译的语言，同样也是第二级子目录的名称”zh”。
       上面的命令就可以创建一个中文的po翻译文件了，文件会保存在当前目录下的”translations/zh/LC_MESSAGES”下，文件名为”messages.po”。

    5、打开刚才生成的中文po翻译文件，将我们要翻译的内容写入”msgstr”项中，并保存

    6、最后一步，编译po文件，并生成”*.mo”文件
        pybabel compile -d ./app/translations
        “-d”指定了翻译文件存放的子目录。该命令执行后，”translations”目录下的所有po文件都会被编译成mo文件

    7、之后，如果代码中的待翻译的文字被更改过，我们需要重新生成”messages.pot”翻译文件模板。
       此时，要是再通过”pybabel init”命令来创建po文件的话，会丢失之前已翻译好的内容，这个损失是很大的，其实我们可以通过下面的方法来更新po文件：
       pybabel update -i messages.pot -d translations
       执行”pybabel update”后，原先的翻译会被保留。不过要注意，因为有些字条pybabel无法确定，会将其标为”fuzzy”，你要将”fuzzy”注释去掉才能使其起效。

       最后的最后，提醒下大家，translations目录必须是跟你 Flask 的app应用对象在同一目录下，如果你的app对象是放在某个包里，那translations目录也必须放在那个包下。

   2、





