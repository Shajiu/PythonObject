# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: watermark.py
# @Time    : 2021/10/18 19:43


from watermarker.marker import add_mark

add_mark(r"D:\personal\gitpython\maoyan\0.png", "源码上门取算法码上到", angle=15, size=20, space=40, color='#c5094d')

from filediff.diff import file_diff_compare

file_diff_compare(r"E:\blog\Shajiu.github.io\source\_posts\完美-两行代码便能对图像加水印、文件对比以及利好抓包\\一线城市1.log",
                  r"E:\blog\Shajiu.github.io\source\_posts\完美-两行代码便能对图像加水印、文件对比以及利好抓包\\一线城市2.log",
                  diff_out="diff_result.html", show_all=True, max_width=70, numlines=0, no_browser=True)

from curl2py.curlParseTool import curlCmdGenPyScript

curl_cmd="curl 'https://sp1.baidu.com/5bU_dTmfKgQFm2e88IuM_a/w.gif?q=python&fm=se&T=1634558960&y=FF7C7C76&rsv_cache=0&rsv_tpfail=1&rsv_pstg=20&rsv_prw=python&rsv_svoice=0&rsv_pre=1&rsv_reh=93_158_273_116_166_376_74_72_116_231_116|527_346&rsv_scr=1920_2523_0_0_1080_1920&rsv_psid=5F868DDA83411962039CD866191DDDDE&rsv_pstm=1634439053&rsv_idc=7&rsv_sid=&cid=0&qid=ce8aa8df00007cd7&t=1634558962150&rsv_pstg=20&rsv_cftime=1&rsv_iorr=0&rsv_tn=baidu&rsv_isid=34439_34067_31254_34742_34584_34505_34707_34747_26350_34828_22157_34691_34673&rsv_ssl=1&path=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3Dpython%26fenlei%3D256%26oq%3Dpython%26rsv_pq%3De9b18c520000bf6d%26rsv_t%3D87b8ZtVBOT9t0so5eKMGSS%252BvF3xX5ffUxf%252Fq0tXK0BVEAvxWRQ2jQ7ssJLM%26rqlang%3Dcn%26rsv_dl%3Dtb%26rsv_enter%3D0%26rsv_btype%3Dt%26prefixsug%3Dpython%26rsp%3D5&rsv_did=6c8b12e00ea4e79cab575a468d3d348e' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: \"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36' \
  -H 'sec-ch-ua-platform: \"Windows\"' \
  -H 'Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: no-cors' \
  -H 'Sec-Fetch-Dest: image' \
  -H 'Referer: https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&fenlei=256&oq=python&rsv_pq=e9b18c520000bf6d&rsv_t=87b8ZtVBOT9t0so5eKMGSS%2BvF3xX5ffUxf%2Fq0tXK0BVEAvxWRQ2jQ7ssJLM&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_btype=t&prefixsug=python&rsp=5' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Cookie: BIDUPSID=5F868DDA83411962039CD866191DDDDE; PSTM=1634439053; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=438F7829A5218E07B65F452D698879A9:FG=1; H_PS_PSSID=; __yjs_duid=1_24bd4a27f3a1725b417affeecaa43b6c1634543199744; delPer=0; PSINO=1; BAIDUID_BFESS=438F7829A5218E07B65F452D698879A9:FG=1' \
  --compressed"
output = curlCmdGenPyScript(curl_cmd)
print(output)