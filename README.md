本脚本通过修改 [zhy201810576/ETagCN](https://github.com/zhy201810576/ETagCN) 实现，也为他人可能有的其他需求提供改写的思路  
由于Lanraragi的数据库导入导出功能有很多的问题，因此，使用插件来进行Tag会比通过导入json数据导入source再进行Tag的方法容易且便捷的多  
本脚本的逻辑为，通过识别压缩包的名字。因此，需要将压缩包的名字改为gid-token-*的形式，此条件可以通过python和Ehviewer的数据库来实现。  
然而，可能存在不是通过Ehviewer来下载的情况。这里，我的python命名规则为，由于Ehviewer下载的文件夹的名字为：gid-名字。因此可以先获取gid,通过Ehviewer数据库获取到token,在进行重命名。如果不通过Ehviewer的，通过gid是获取不到token的，因此将返回"None"。因此，如果只要文件名中含有"-None"的表明此文件很有可能不是来自于Ehviewer的，因此进行图片识别。  
但此方法仍可能出问题，如果非Ehviewer文件中中不含有"-"可能就会报错。因此如果有更好的想法，或者希望能自己定义压缩包名字，可以自行更改代码，这里将提供一种思路。  
通过修改原代码中80行起的代码，原代码为else引导的使用封面进行图片搜索的匹配。修改为如果文件名中含有"-None"再进行图片搜索  
否则认为通过的所有的文件都是可以通过文件名获取了gid和token  
总之不管这么改，如果要使用Eh来进行Tag,就必须要知道gid和token的值

```perl
    } elsif ( $lrr_info->{archive_title} =~ /-None/ ) { 
        $logger->debug("标题内无gid,token或token在数据库中不存在，因此将使用图片匹配功能进行");
        # Craft URL for Text Search on EH if there's no user argument
        ( $gID, $gToken ) = &lookup_gallery(
            $lrr_info->{archive_title},
            $lrr_info->{existing_tags},
            $lrr_info->{thumbnail_hash},
            $ua, $domain, $lang, $usethumbs, $expunged
        );
    } else {
        my @title_Array = split(/-/, $lrr_info->{archive_title} );  
        $gID = $title_Array[0];
        $gToken = $title_Array[1];
        $logger->debug("Skipping search and using gallery $gID / $gToken from Archive Name");
    }
 ```
