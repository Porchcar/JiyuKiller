# -*- encoding:utf-8 -*-
VERSION = "2.0 Preview"
VERSION_PROMPT = "JiyuKiller1.0.0 Command Line Version"
def autoinstall(name:str):
    print(f"Error when importing {name}, auto installing...")
    os.system(f"pip install {name}")
    print(f"{name} installed successfully")

ICON = "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+P8okvj/KpT4/yqU+P8okfb/KJH2/yiR9v8mi/P/Jovz/yaL8/8jhfD/I4Xw/x577f8ee+3/Hnvt/xZo6f8WaOn/Fmjp/w1S5v8NUub/CkLT/wpC0/8KQtP/F0GX/xdBl/8XQZf/CRs/eAkbP3gAAAAYAAAAGAAAABgCBxESAgcREgIHERIWQJb3FkCW9x9ewf8fXsH/H17B/y6S+f8ukvn/LpL5/zCZ+v8wmfr/L5r6/y+a+v8vmvr/Lpr6/y6a+v8umvr/LZn6/y2Z+v8smfn/LJn5/yyZ+f8smPn/LJj5/yyY+f8smfn/LJn5/yyZ+v8smfr/LJn6/yyZ+v8smfr/LJn6/yuW+v8rlvr/KJH5/yiR+f8okfn/JYr5/yWK+f8livn/IH/4/yB/+P9ppfr/aaX6/2ml+v/X5v3/1+b9/9fm/f/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////5+/7/+fv+/7DP/P+wz/z/sM/8/z6N+P8+jfj/Po34/yCB+P8ggfj/IoT4/yKE+P8ihPj/IoT4/yKE+P8ihPj/gLr7/4C6+/8mjPj/Joz4/yaM+P8okvj/KJL4/yiS+P8qlPj/KpT4/yiR9v8okfb/KJH2/yaL8/8mi/P/Jovz/yOF8P8jhfD/Hnvt/x577f8ee+3/Fmjp/xZo6f8WaOn/DVLm/w1S5v8KQtP/CkLT/wpC0/8XQZf/F0GX/xdBl/8JGz94CRs/eAAAABgAAAAYAAAAGAIHERICBxESAgcREhZAlvcWQJb3H17B/x9ewf8fXsH/LpL5/y6S+f8ukvn/MJn6/zCZ+v8vmvr/L5r6/y+a+v8umvr/Lpr6/y6a+v8tmfr/LZn6/yyZ+f8smfn/LJn5/yyY+f8smPn/LJj5/yyZ+f8smfn/LJn6/yyZ+v8smfr/LJn6/yyZ+v8smfr/K5b6/yuW+v8okfn/KJH5/yiR+f8livn/JYr5/yWK+f8gf/j/IH/4/2ml+v9ppfr/aaX6/9fm/f/X5v3/1+b9//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////n7/v/5+/7/sM/8/7DP/P+wz/z/Po34/z6N+P8+jfj/IIH4/yCB+P8ihPj/IoT4/yKE+P8ihPj/IoT4/yKE+P+Auvv/gLr7/yaM+P8mjPj/Joz4/yiS+P8okvj/KJL4/yqU+P8qlPj/KJH2/yiR9v8okfb/Jovz/yaL8/8mi/P/I4Xw/yOF8P8ee+3/Hnvt/x577f8WaOn/Fmjp/xZo6f8NUub/DVLm/wpC0/8KQtP/CkLT/xdBl/8XQZf/F0GX/wkbP3gJGz94AAAAGAAAABgAAAAYChxCRgocQkYKHEJGF0GX/xdBl/8rd93/K3fd/yt33f82l/r/Npf6/zaX+v81mvn/NZr5/zKZ+f8ymfn/Mpn5/y+Y+f8vmPn/L5j5/yyW+f8slvn/KJT5/yiU+f8olPn/JpP5/yaT+f8mk/n/JpP5/yaT+f8mkvn/JpL5/yaS+f8lkPn/JZD5/yWQ+f8iivj/Ior4/x5/+P8ef/j/Hn/4/0iR+f9Ikfn/SJH5/9Lj/f/S4/3////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////6/P7/+vz+//r8/v+ewvv/nsL7/yBy9/8gcvf/IHL3/53C+/+dwvv/ncL7//7+///+/v//KYX4/ymF+P8phfj/Ion4/yKJ+P8iifj/JZD4/yWQ+P8kjvb/JI72/ySO9v8iifT/Ion0/yKJ9P8ghPH/IITx/x197/8dfe//HX3v/xdv6/8Xb+v/F2/r/w9a6P8PWuj/CEXl/whF5f8IReX/FkCc/xZAnP8WQJz/Dypiqw8qYqsAAAAeAAAAHgAAAB4KHEJGChxCRgocQkYXQZf/F0GX/yt33f8rd93/K3fd/zaX+v82l/r/Npf6/zWa+f81mvn/Mpn5/zKZ+f8ymfn/L5j5/y+Y+f8vmPn/LJb5/yyW+f8olPn/KJT5/yiU+f8mk/n/JpP5/yaT+f8mk/n/JpP5/yaS+f8mkvn/JpL5/yWQ+f8lkPn/JZD5/yKK+P8iivj/Hn/4/x5/+P8ef/j/SJH5/0iR+f9Ikfn/0uP9/9Lj/f////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////r8/v/6/P7/+vz+/57C+/+ewvv/IHL3/yBy9/8gcvf/ncL7/53C+/+dwvv//v7///7+//8phfj/KYX4/ymF+P8iifj/Ion4/yKJ+P8lkPj/JZD4/ySO9v8kjvb/JI72/yKJ9P8iifT/Ion0/yCE8f8ghPH/HX3v/x197/8dfe//F2/r/xdv6/8Xb+v/D1ro/w9a6P8IReX/CEXl/whF5f8WQJz/FkCc/xZAnP8PKmKrDypiqwAAAB4AAAAeAAAAHgocQkYKHEJGChxCRhdBl/8XQZf/K3fd/yt33f8rd93/Npf6/zaX+v82l/r/NZr5/zWa+f8ymfn/Mpn5/zKZ+f8vmPn/L5j5/y+Y+f8slvn/LJb5/yiU+f8olPn/KJT5/yaT+f8mk/n/JpP5/yaT+f8mk/n/JpL5/yaS+f8mkvn/JZD5/yWQ+f8lkPn/Ior4/yKK+P8ef/j/Hn/4/x5/+P9Ikfn/SJH5/0iR+f/S4/3/0uP9////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////+vz+//r8/v/6/P7/nsL7/57C+/8gcvf/IHL3/yBy9/+dwvv/ncL7/53C+//+/v///v7//ymF+P8phfj/KYX4/yKJ+P8iifj/Ion4/yWQ+P8lkPj/JI72/ySO9v8kjvb/Ion0/yKJ9P8iifT/IITx/yCE8f8dfe//HX3v/x197/8Xb+v/F2/r/xdv6/8PWuj/D1ro/whF5f8IReX/CEXl/xZAnP8WQJz/FkCc/w8qYqsPKmKrAAAAHgAAAB4AAAAeCyBKdgsgSnYLIEp2F0GX/xdBl/85jfL/OY3y/zmN8v87mfr/O5n6/zuZ+v84mfr/OJn6/zSY+f80mPn/NJj5/zCV+f8wlfn/MJX5/yqS+f8qkvn/JI/5/ySP+f8kj/n/II35/yCN+f8gjfn/II35/yCN+f8fivn/H4r5/x+K+f8dhPj/HYT4/x2E+P8Yeff/GHn3/3Gn+v9xp/r/caf6//r7/v/6+/7/+vv+//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////D1/v/w9f7/8PX+////////////////////////////SJD4/0iQ+P9IkPj/G4D4/xuA+P8bgPj/H4r4/x+K+P8fivf/H4r3/x+K9/8dhvX/HYb1/x2G9f8cgfL/HIHy/xp88P8afPD/Gnzw/xZy7f8Wcu3/FnLt/xBf6v8QX+r/CEnn/whJ5/8ISef/EkCq/xJAqv8SQKr/FDqG0RQ6htEAAAAiAAAAIgAAACILIEp2CyBKdgsgSnYXQZf/F0GX/zmN8v85jfL/OY3y/zuZ+v87mfr/O5n6/ziZ+v84mfr/NJj5/zSY+f80mPn/MJX5/zCV+f8wlfn/KpL5/yqS+f8kj/n/JI/5/ySP+f8gjfn/II35/yCN+f8gjfn/II35/x+K+f8fivn/H4r5/x2E+P8dhPj/HYT4/xh59/8Yeff/caf6/3Gn+v9xp/r/+vv+//r7/v/6+/7/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////8PX+//D1/v/w9f7///////////////////////////9IkPj/SJD4/0iQ+P8bgPj/G4D4/xuA+P8fivj/H4r4/x+K9/8fivf/H4r3/x2G9f8dhvX/HYb1/xyB8v8cgfL/Gnzw/xp88P8afPD/FnLt/xZy7f8Wcu3/EF/q/xBf6v8ISef/CEnn/whJ5/8SQKr/EkCq/xJAqv8UOobRFDqG0QAAACIAAAAiAAAAIhM2fZUTNn2VEzZ9lRlGnf8ZRp3/Q5f5/0OX+f9Dl/n/QZv6/0Gb+v9Bm/r/PJn6/zyZ+v83lvr/N5b6/zeW+v8wk/n/MJP5/zCT+f8oj/n/KI/5/yCK+f8givn/IIr5/xuH+f8bh/n/G4f5/xqF+f8ahfn/F3/4/xd/+P8Xf/j/FHT3/xR09/8UdPf/eqv6/3qr+v///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////2yi+v9sovr/bKL6/xV4+P8VePj/FXj4/xmD+f8Zg/n/GYX3/xmF9/8Zhff/GIL2/xiC9v8Ygvb/F370/xd+9P8WevH/Fnrx/xZ68f8Tcu//E3Lv/xNy7/8PYuv/D2Lr/whM6f8ITOn/CEzp/xBAtv8QQLb/EEC2/xY+kekWPpHpAAAAJAAAACQAAAAkEzZ9lRM2fZUTNn2VGUad/xlGnf9Dl/n/Q5f5/0OX+f9Bm/r/QZv6/0Gb+v88mfr/PJn6/zeW+v83lvr/N5b6/zCT+f8wk/n/MJP5/yiP+f8oj/n/IIr5/yCK+f8givn/G4f5/xuH+f8bh/n/GoX5/xqF+f8Xf/j/F3/4/xd/+P8UdPf/FHT3/xR09/96q/r/eqv6////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////bKL6/2yi+v9sovr/FXj4/xV4+P8VePj/GYP5/xmD+f8Zhff/GYX3/xmF9/8Ygvb/GIL2/xiC9v8XfvT/F370/xZ68f8WevH/Fnrx/xNy7/8Tcu//E3Lv/w9i6/8PYuv/CEzp/whM6f8ITOn/EEC2/xBAtv8QQLb/Fj6R6RY+kekAAAAkAAAAJAAAACQTNn2VEzZ9lRM2fZUZRp3/GUad/0OX+f9Dl/n/Q5f5/0Gb+v9Bm/r/QZv6/zyZ+v88mfr/N5b6/zeW+v83lvr/MJP5/zCT+f8wk/n/KI/5/yiP+f8givn/IIr5/yCK+f8bh/n/G4f5/xuH+f8ahfn/GoX5/xd/+P8Xf/j/F3/4/xR09/8UdPf/FHT3/3qr+v96q/r///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////9sovr/bKL6/2yi+v8VePj/FXj4/xV4+P8Zg/n/GYP5/xmF9/8Zhff/GYX3/xiC9v8Ygvb/GIL2/xd+9P8XfvT/Fnrx/xZ68f8WevH/E3Lv/xNy7/8Tcu//D2Lr/w9i6/8ITOn/CEzp/whM6f8QQLb/EEC2/xBAtv8WPpHpFj6R6QAAACQAAAAkAAAAJBY+jKEWPoyhFj6MoR1MpP8dTKT/Spv6/0qb+v9Km/r/R536/0ed+v9Hnfr/QJr6/0Ca+v85lvr/OZb6/zmW+v8wkfr/MJH6/zCR+v8njPn/J4z5/x2H+f8dh/n/HYf5/xaC+f8Wgvn/FoL5/xN9+P8Tffj/EHP3/xBz9/8Qc/f/Wpb5/1qW+f9alvn//f7///3+////////////////////////////////////////////////////////////////////////////////////////5u7+/+bu/v/m7v7/nb/7/52/+/+dv/v/baH6/22h+v9Vkvn/VZL5/1WS+f9hmfn/YZn5/2GZ+f99q/r/fav6/8LW/P/C1vz/wtb8//v8/v/7/P7/+/z+/////////////////////////////////////////////////////////////////////////////////////////////////5K5+/+Sufv/krn7/xBx9/8Qcff/EHH3/xN++P8Tfvj/FIH4/xSB+P8Ugfj/FH72/xR+9v8Ufvb/E3v0/xN79P8SePL/Enjy/xJ48v8RcvH/EXLx/xFy8f8NY+7/DWPu/whO6v8ITur/CE7q/w9Buv8PQbr/D0G6/xY/lPMWP5TzAAAAIgAAACIAAAAiFj6MoRY+jKEWPoyhHUyk/x1MpP9Km/r/Spv6/0qb+v9Hnfr/R536/0ed+v9Amvr/QJr6/zmW+v85lvr/OZb6/zCR+v8wkfr/MJH6/yeM+f8njPn/HYf5/x2H+f8dh/n/FoL5/xaC+f8Wgvn/E334/xN9+P8Qc/f/EHP3/xBz9/9alvn/Wpb5/1qW+f/9/v///f7////////////////////////////////////////////////////////////////////////////////////////m7v7/5u7+/+bu/v+dv/v/nb/7/52/+/9tofr/baH6/1WS+f9Vkvn/VZL5/2GZ+f9hmfn/YZn5/32r+v99q/r/wtb8/8LW/P/C1vz/+/z+//v8/v/7/P7/////////////////////////////////////////////////////////////////////////////////////////////////krn7/5K5+/+Sufv/EHH3/xBx9/8Qcff/E374/xN++P8Ugfj/FIH4/xSB+P8Ufvb/FH72/xR+9v8Te/T/E3v0/xJ48v8SePL/Enjy/xFy8f8RcvH/EXLx/w1j7v8NY+7/CE7q/whO6v8ITur/D0G6/w9Buv8PQbr/Fj+U8xY/lPMAAAAiAAAAIgAAACIWPoyhFj6MoRY+jKEdTKT/HUyk/0qb+v9Km/r/Spv6/0ed+v9Hnfr/R536/0Ca+v9Amvr/OZb6/zmW+v85lvr/MJH6/zCR+v8wkfr/J4z5/yeM+f8dh/n/HYf5/x2H+f8Wgvn/FoL5/xaC+f8Tffj/E334/xBz9/8Qc/f/EHP3/1qW+f9alvn/Wpb5//3+///9/v///////////////////////////////////////////////////////////////////////////////////////+bu/v/m7v7/5u7+/52/+/+dv/v/nb/7/22h+v9tofr/VZL5/1WS+f9Vkvn/YZn5/2GZ+f9hmfn/fav6/32r+v/C1vz/wtb8/8LW/P/7/P7/+/z+//v8/v////////////////////////////////////////////////////////////////////////////////////////////////+Sufv/krn7/5K5+/8Qcff/EHH3/xBx9/8Tfvj/E374/xSB+P8Ugfj/FIH4/xR+9v8Ufvb/FH72/xN79P8Te/T/Enjy/xJ48v8SePL/EXLx/xFy8f8RcvH/DWPu/w1j7v8ITur/CE7q/whO6v8PQbr/D0G6/w9Buv8WP5TzFj+U8wAAACIAAAAiAAAAIhc/jJsXP4ybFz+Mmx1Mo/8dTKP/UZ36/1Gd+v9Rnfr/TZ/6/02f+v9Nn/r/RZv6/0Wb+v88lvn/PJb5/zyW+f8ykPn/MpD5/zKQ+f8nivn/J4r5/xqD+P8ag/j/GoP4/xF8+P8RfPj/EXz4/w1z9/8Nc/f/JHX3/yR19/8kdff/7/T+/+/0/v/v9P7//////////////////////////////////////////////////////////////////////+fv/v/n7/7/5+/+/2md+f9pnfn/Dmb2/w5m9v8OZvb/DGr3/wxq9/8Mavf/DW73/w1u9/8NcPf/DXD3/w1w9/8Nb/f/DW/3/w1v9/8MbPf/DGz3/wpk9v8KZPb/CmT2/y5z9/8uc/f/LnP3/7DH+/+wx/v//////////////////////////////////////////////////////////////////////////////////////7zS/P+80vz/vNL8/wxq9/8Mavf/DGr3/w53+P8Od/j/EH34/xB9+P8Qffj/D3r2/w969v8Pevb/Dnj1/w549f8OdfP/DnXz/w518/8NcPH/DXDx/w1w8f8KY+7/CmPu/wZO6/8GTuv/Bk7r/w9AuP8PQLj/D0C4/xY/kusWP5LrAAAAHgAAAB4AAAAeFz+Mmxc/jJsXP4ybHUyj/x1Mo/9Rnfr/UZ36/1Gd+v9Nn/r/TZ/6/02f+v9Fm/r/RZv6/zyW+f88lvn/PJb5/zKQ+f8ykPn/MpD5/yeK+f8nivn/GoP4/xqD+P8ag/j/EXz4/xF8+P8RfPj/DXP3/w1z9/8kdff/JHX3/yR19//v9P7/7/T+/+/0/v//////////////////////////////////////////////////////////////////////5+/+/+fv/v/n7/7/aZ35/2md+f8OZvb/Dmb2/w5m9v8Mavf/DGr3/wxq9/8Nbvf/DW73/w1w9/8NcPf/DXD3/w1v9/8Nb/f/DW/3/wxs9/8MbPf/CmT2/wpk9v8KZPb/LnP3/y5z9/8uc/f/sMf7/7DH+///////////////////////////////////////////////////////////////////////////////////////vNL8/7zS/P+80vz/DGr3/wxq9/8Mavf/Dnf4/w53+P8Qffj/EH34/xB9+P8Pevb/D3r2/w969v8OePX/Dnj1/w518/8OdfP/DnXz/w1w8f8NcPH/DXDx/wpj7v8KY+7/Bk7r/wZO6/8GTuv/D0C4/w9AuP8PQLj/Fj+S6xY/kusAAAAeAAAAHgAAAB4RLWOBES1jgREtY4EbSJ7/G0ie/1We9/9Vnvf/VZ73/1Oi+v9Tovr/U6L6/0yd+v9Mnfr/QZj5/0GY+f9BmPn/NZH5/zWR+f81kfn/KIr5/yiK+f8Zgfj/GYH4/xmB+P8Odvf/Dnb3/w529/8Jafb/CWn2/6bF+/+mxfv/psX7///////////////////////////////////////////////////////////////////////H2vz/x9r8/8fa/P8bbfb/G232/xtt9v8Iafb/CGn2/wlw9/8JcPf/CXD3/wp09/8KdPf/CnT3/wp2+P8Kdvj/Cnf4/wp3+P8Kd/j/Cnf4/wp3+P8Kd/j/CnT3/wp09/8Jbff/CW33/wlt9/8NZPb/DWT2/w1k9v+0y/v/tMv7///////////////////////////////////////////////////////////////////////////////////////l7f7/5e3+/+Xt/v8HZfb/B2X2/wdl9v8Jc/f/CXP3/wt59/8Leff/C3n3/wp49v8KePb/Cnj2/wp19P8KdfT/CnPz/wpz8/8Kc/P/CW/x/wlv8f8Jb/H/B2Lv/wdi7/8FTuz/BU7s/wVO7P8RQK//EUCv/xFAr/8VPIzTFTyM0wAAABoAAAAaAAAAGhEtY4ERLWOBES1jgRtInv8bSJ7/VZ73/1We9/9Vnvf/U6L6/1Oi+v9Tovr/TJ36/0yd+v9BmPn/QZj5/0GY+f81kfn/NZH5/zWR+f8oivn/KIr5/xmB+P8Zgfj/GYH4/w529/8Odvf/Dnb3/wlp9v8Jafb/psX7/6bF+/+mxfv//////////////////////////////////////////////////////////////////////8fa/P/H2vz/x9r8/xtt9v8bbfb/G232/whp9v8Iafb/CXD3/wlw9/8JcPf/CnT3/wp09/8KdPf/Cnb4/wp2+P8Kd/j/Cnf4/wp3+P8Kd/j/Cnf4/wp3+P8KdPf/CnT3/wlt9/8Jbff/CW33/w1k9v8NZPb/DWT2/7TL+/+0y/v//////////////////////////////////////////////////////////////////////////////////////+Xt/v/l7f7/5e3+/wdl9v8HZfb/B2X2/wlz9/8Jc/f/C3n3/wt59/8Leff/Cnj2/wp49v8KePb/CnX0/wp19P8Kc/P/CnPz/wpz8/8Jb/H/CW/x/wlv8f8HYu//B2Lv/wVO7P8FTuz/BU7s/xFAr/8RQK//EUCv/xU8jNMVPIzTAAAAGgAAABoAAAAaES1jgREtY4ERLWOBG0ie/xtInv9Vnvf/VZ73/1We9/9Tovr/U6L6/1Oi+v9Mnfr/TJ36/0GY+f9BmPn/QZj5/zWR+f81kfn/NZH5/yiK+f8oivn/GYH4/xmB+P8Zgfj/Dnb3/w529/8Odvf/CWn2/wlp9v+mxfv/psX7/6bF+///////////////////////////////////////////////////////////////////////x9r8/8fa/P/H2vz/G232/xtt9v8bbfb/CGn2/whp9v8JcPf/CXD3/wlw9/8KdPf/CnT3/wp09/8Kdvj/Cnb4/wp3+P8Kd/j/Cnf4/wp3+P8Kd/j/Cnf4/wp09/8KdPf/CW33/wlt9/8Jbff/DWT2/w1k9v8NZPb/tMv7/7TL+///////////////////////////////////////////////////////////////////////////////////////5e3+/+Xt/v/l7f7/B2X2/wdl9v8HZfb/CXP3/wlz9/8Leff/C3n3/wt59/8KePb/Cnj2/wp49v8KdfT/CnX0/wpz8/8Kc/P/CnPz/wlv8f8Jb/H/CW/x/wdi7/8HYu//BU7s/wVO7P8FTuz/EUCv/xFAr/8RQK//FTyM0xU8jNMAAAAaAAAAGgAAABoaP31WGj99Vho/fVYbSqD/G0qg/1CS6f9Qkun/UJLp/1mk+v9ZpPr/WaT6/1Gg+v9RoPr/Rpr6/0aa+v9Gmvr/OZL5/zmS+f85kvn/Kor5/yqK+f8af/j/Gn/4/xp/+P8McPf/DHD3/wxw9/8ueff/Lnn3//3+///9/v///f7/////////////////////////////////////////////////////////////0+H9/9Ph/f8SZvb/Emb2/xJm9v8Gavb/Bmr2/wZq9v8Hcff/B3H3/wd1+P8Hdfj/B3X4/wd3+P8Hd/j/B3f4/wd3+P8Hd/j/B3f4/wd3+P8Hd/j/B3f4/wd3+P8Hd/j/B3X4/wd1+P8Gb/f/Bm/3/wZv9/+bwvz/m8L8/5vC/P/////////////////////////////////////////////////////////////////////////////////////////////////+/v///v7///7+//8Rafb/EWn2/xFp9v8Gb/f/Bm/3/wd19/8Hdff/B3X3/wd19v8Hdfb/B3X2/wdz9f8Hc/X/BnHz/wZx8/8GcfP/Bmzy/wZs8v8GbPL/BWDw/wVg8P8CTO3/Akzt/wJM7f8UQaD/FEGg/xRBoP8SM3itEjN4rQAAABIAAAASAAAAEho/fVYaP31WGj99VhtKoP8bSqD/UJLp/1CS6f9Qkun/WaT6/1mk+v9ZpPr/UaD6/1Gg+v9Gmvr/Rpr6/0aa+v85kvn/OZL5/zmS+f8qivn/Kor5/xp/+P8af/j/Gn/4/wxw9/8McPf/DHD3/y559/8ueff//f7///3+///9/v/////////////////////////////////////////////////////////////T4f3/0+H9/xJm9v8SZvb/Emb2/wZq9v8Gavb/Bmr2/wdx9/8Hcff/B3X4/wd1+P8Hdfj/B3f4/wd3+P8Hd/j/B3f4/wd3+P8Hd/j/B3f4/wd3+P8Hd/j/B3f4/wd3+P8Hdfj/B3X4/wZv9/8Gb/f/Bm/3/5vC/P+bwvz/m8L8//////////////////////////////////////////////////////////////////////////////////////////////////7+///+/v///v7//xFp9v8Rafb/EWn2/wZv9/8Gb/f/B3X3/wd19/8Hdff/B3X2/wd19v8Hdfb/B3P1/wdz9f8GcfP/BnHz/wZx8/8GbPL/Bmzy/wZs8v8FYPD/BWDw/wJM7f8CTO3/Akzt/xRBoP8UQaD/FEGg/xIzeK0SM3itAAAAEgAAABIAAAASGj99Vho/fVYaP31WG0qg/xtKoP9Qkun/UJLp/1CS6f9ZpPr/WaT6/1mk+v9RoPr/UaD6/0aa+v9Gmvr/Rpr6/zmS+f85kvn/OZL5/yqK+f8qivn/Gn/4/xp/+P8af/j/DHD3/wxw9/8McPf/Lnn3/y559//9/v///f7///3+/////////////////////////////////////////////////////////////9Ph/f/T4f3/Emb2/xJm9v8SZvb/Bmr2/wZq9v8Gavb/B3H3/wdx9/8Hdfj/B3X4/wd1+P8Hd/j/B3f4/wd3+P8Hd/j/B3f4/wd3+P8Hd/j/B3f4/wd3+P8Hd/j/B3f4/wd1+P8Hdfj/Bm/3/wZv9/8Gb/f/m8L8/5vC/P+bwvz//////////////////////////////////////////////////////////////////////////////////////////////////v7///7+///+/v//EWn2/xFp9v8Rafb/Bm/3/wZv9/8Hdff/B3X3/wd19/8Hdfb/B3X2/wd19v8Hc/X/B3P1/wZx8/8GcfP/BnHz/wZs8v8GbPL/Bmzy/wVg8P8FYPD/Akzt/wJM7f8CTO3/FEGg/xRBoP8UQaD/EjN4rRIzeK0AAAASAAAAEgAAABIjUJcaI1CXGiNQlxodTKL/HUyi/0B80v9AfNL/QHzS/1yl+v9cpfr/XKX6/1Sh+v9Uofr/SJv6/0ib+v9Im/r/O5P5/zuT+f87k/n/K4v5/yuL+f8afvj/Gn74/xp++P8La/b/C2v2/wtr9v+TuPv/k7j7/////////////////////////////////////////////////////////////P3///z9///8/f//L3f3/y939/8DZ/b/A2f2/wNn9v8Ecff/BHH3/wRx9/8Edfj/BHX4/wR1+P8Edfj/BHX4/wR2+P8Edvj/BHb4/wR2+P8Edvj/BHb4/wR2+P8Edvj/BHb4/wR2+P8Edvj/BHT4/wR0+P8Ecff/BHH3/wRx9/8Da/f/A2v3/wNr9/8Sbff/Em33/z+E+P8/hPj/P4T4/2ic+f9onPn/aJz5/5C1+v+Qtfr/vdL8/73S/P+90vz/5u3+/+bt/v/m7f7///////////////////////////8zgPf/M4D3/zOA9/8EbPb/BGz2/wRy9v8Ecvb/BHL2/wRy9v8Ecvb/BHL2/wRx9f8EcfX/BG/z/wRv8/8Eb/P/A2ry/wNq8v8DavL/A1zw/wNc8P8FSeD/BUng/wVJ4P8XQZf/F0GX/xdBl/8KHkZyCh5GcgINIgwCDSIMAg0iDCNQlxojUJcaI1CXGh1Mov8dTKL/QHzS/0B80v9AfNL/XKX6/1yl+v9cpfr/VKH6/1Sh+v9Im/r/SJv6/0ib+v87k/n/O5P5/zuT+f8ri/n/K4v5/xp++P8afvj/Gn74/wtr9v8La/b/C2v2/5O4+/+TuPv////////////////////////////////////////////////////////////8/f///P3///z9//8vd/f/L3f3/wNn9v8DZ/b/A2f2/wRx9/8Ecff/BHH3/wR1+P8Edfj/BHX4/wR1+P8Edfj/BHb4/wR2+P8Edvj/BHb4/wR2+P8Edvj/BHb4/wR2+P8Edvj/BHb4/wR2+P8EdPj/BHT4/wRx9/8Ecff/BHH3/wNr9/8Da/f/A2v3/xJt9/8Sbff/P4T4/z+E+P8/hPj/aJz5/2ic+f9onPn/kLX6/5C1+v+90vz/vdL8/73S/P/m7f7/5u3+/+bt/v///////////////////////////zOA9/8zgPf/M4D3/wRs9v8EbPb/BHL2/wRy9v8Ecvb/BHL2/wRy9v8Ecvb/BHH1/wRx9f8Eb/P/BG/z/wRv8/8DavL/A2ry/wNq8v8DXPD/A1zw/wVJ4P8FSeD/BUng/xdBl/8XQZf/F0GX/woeRnIKHkZyAg0iDAINIgwCDSIMMmm5AjJpuQIyabkCHk2hzR5Noc0qX7X/Kl+1/ypftf9bpfr/W6X6/1ul+v9Uovr/VKL6/0ic+v9InPr/SJz6/zuU+f87lPn/O5T5/yyL+f8si/n/Gnz4/xp8+P8afPj/Cmb2/wpm9v8KZvb/4uv9/+Lr/f///////////////////////////////////////////////////////////6LB+/+iwfv/osH7/wFi9v8BYvb/AW33/wFt9/8Bbff/AXP4/wFz+P8Bc/j/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF0+P8BdPj/AXP4/wFz+P8Bc/j/AXD3/wFw9/8BcPf/AW33/wFt9/8Baff/AWn3/wFp9/8BZPb/AWT2/wFk9v8BX/T/AV/0/wFZ8/8BWfP/AVnz/wFU8v8BVPL/AVTy/xFe8/8RXvP/PoD1/z6A9f8+gPX/GnD0/xpw9P8acPT/AWj0/wFo9P8BbvX/AW71/wFu9f8Bb/X/AW/1/wFv9f8Bb/T/AW/0/wFt8/8BbfP/AW3z/wFm8f8BZvH/AWbx/wFX7/8BV+//DETB/wxEwf8MRMH/F0CW+xdAlvsXQJb7BAsbKgQLGyoFGEAGBRhABgUYQAYyabkCMmm5AjJpuQIeTaHNHk2hzSpftf8qX7X/Kl+1/1ul+v9bpfr/W6X6/1Si+v9Uovr/SJz6/0ic+v9InPr/O5T5/zuU+f87lPn/LIv5/yyL+f8afPj/Gnz4/xp8+P8KZvb/Cmb2/wpm9v/i6/3/4uv9////////////////////////////////////////////////////////////osH7/6LB+/+iwfv/AWL2/wFi9v8Bbff/AW33/wFt9/8Bc/j/AXP4/wFz+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXT4/wF0+P8Bc/j/AXP4/wFz+P8BcPf/AXD3/wFw9/8Bbff/AW33/wFp9/8Baff/AWn3/wFk9v8BZPb/AWT2/wFf9P8BX/T/AVnz/wFZ8/8BWfP/AVTy/wFU8v8BVPL/EV7z/xFe8/8+gPX/PoD1/z6A9f8acPT/GnD0/xpw9P8BaPT/AWj0/wFu9f8BbvX/AW71/wFv9f8Bb/X/AW/1/wFv9P8Bb/T/AW3z/wFt8/8BbfP/AWbx/wFm8f8BZvH/AVfv/wFX7/8MRMH/DETB/wxEwf8XQJb7F0CW+xdAlvsECxsqBAsbKgUYQAYFGEAGBRhABjJpuQIyabkCMmm5Ah5Noc0eTaHNKl+1/ypftf8qX7X/W6X6/1ul+v9bpfr/VKL6/1Si+v9InPr/SJz6/0ic+v87lPn/O5T5/zuU+f8si/n/LIv5/xp8+P8afPj/Gnz4/wpm9v8KZvb/Cmb2/+Lr/f/i6/3///////////////////////////////////////////////////////////+iwfv/osH7/6LB+/8BYvb/AWL2/wFt9/8Bbff/AW33/wFz+P8Bc/j/AXP4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8Bdfj/AXX4/wF1+P8BdPj/AXT4/wFz+P8Bc/j/AXP4/wFw9/8BcPf/AXD3/wFt9/8Bbff/AWn3/wFp9/8Baff/AWT2/wFk9v8BZPb/AV/0/wFf9P8BWfP/AVnz/wFZ8/8BVPL/AVTy/wFU8v8RXvP/EV7z/z6A9f8+gPX/PoD1/xpw9P8acPT/GnD0/wFo9P8BaPT/AW71/wFu9f8BbvX/AW/1/wFv9f8Bb/X/AW/0/wFv9P8BbfP/AW3z/wFt8/8BZvH/AWbx/wFm8f8BV+//AVfv/wxEwf8MRMH/DETB/xdAlvsXQJb7F0CW+wQLGyoECxsqBRhABgUYQAYFGEAGAAAAAAAAAAAAAAAAG0J/ZhtCf2YfUKX/H1Cl/x9Qpf9Lj+b/S4/m/0uP5v9Tofr/U6H6/0ic+v9InPr/SJz6/zuV+v87lfr/O5X6/yyL+f8si/n/Gnv4/xp7+P8ae/j/KXj3/yl49/8pePf//////////////////////////////////////////////////////////////////////zyB9/88gff/PIH3/wlw9/8JcPf/DX74/w1++P8Nfvj/EYT5/xGE+f8RhPn/E4X5/xOF+f8WiPn/Foj5/xaI+f8WiPn/Foj5/xaI+f8WiPn/Foj5/xaI+f8WiPn/Foj5/xaI+f8WiPn/Foj5/xeJ+f8Xifn/FYf5/xWH+f8Vh/n/EYT5/xGE+f8RhPn/D4D4/w+A+P8Nffj/DX34/w19+P8Hc/b/B3P2/wdz9v8BZvT/AWb0/2Sc9/9knPf/ZJz3/0CA9P9AgPT/QID0/xtk8P8bZPD/AVTv/wFU7/8BVO//AVrx/wFa8f8BWvH/AWPy/wFj8v8BavP/AWrz/wFq8/8BbfT/AW30/wFt9P8BbfP/AW3z/wFr8v8Ba/L/AWvy/wFh8P8BYfD/AWHw/wFQ6v8BUOr/FUGd/xVBnf8VQZ3/EzeBtRM3gbUTN4G1AAAADgAAAA4KLncCCi53AgoudwIAAAAAAAAAAAAAAAAbQn9mG0J/Zh9Qpf8fUKX/H1Cl/0uP5v9Lj+b/S4/m/1Oh+v9Tofr/SJz6/0ic+v9InPr/O5X6/zuV+v87lfr/LIv5/yyL+f8ae/j/Gnv4/xp7+P8pePf/KXj3/yl49///////////////////////////////////////////////////////////////////////PIH3/zyB9/88gff/CXD3/wlw9/8Nfvj/DX74/w1++P8RhPn/EYT5/xGE+f8Thfn/E4X5/xaI+f8WiPn/Foj5/xaI+f8WiPn/Foj5/xaI+f8WiPn/Foj5/xaI+f8WiPn/Foj5/xaI+f8WiPn/F4n5/xeJ+f8Vh/n/FYf5/xWH+f8RhPn/EYT5/xGE+f8PgPj/D4D4/w19+P8Nffj/DX34/wdz9v8Hc/b/B3P2/wFm9P8BZvT/ZJz3/2Sc9/9knPf/QID0/0CA9P9AgPT/G2Tw/xtk8P8BVO//AVTv/wFU7/8BWvH/AVrx/wFa8f8BY/L/AWPy/wFq8/8BavP/AWrz/wFt9P8BbfT/AW30/wFt8/8BbfP/AWvy/wFr8v8Ba/L/AWHw/wFh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tqEuabahNXrO/zV6zv9Gv/v/Rr/7/0a/+/9i1vb/Ytb2/2LW9v9r3PX/a9z1/3Td9f903fX/dN31/3ve+P973vj/e974/1/U/f9f1P3/WdD8/1nQ/P9Z0Pz/VMn7/1TJ+/9Uyfv/Ur/4/1K/+P+Fz/r/hc/6/4XP+v/V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//yfH+/8nx/v/J8f7/h8n5/4fJ+f9TsPb/U7D2/1Ow9v9Rtvf/Ubb3/1G29/9Su/f/Urv3/1K9+P9Svfj/Ur34/1K8+P9SvPj/Urz4/1K59/9Suff/UrX3/1K19/9Stff/fcn4/33J+P99yfj/we79/8Hu/f/V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X5///V+f//eMn5/3jJ+f94yfn/Ur/5/1K/+f9Sv/n/VMn7/1TJ+/9Vzfz/Vc38/1XN/P9Vzvv/Vc77/1XO+/9UzPr/VMz6/1TJ+P9Uyfj/VMn4/zaz9f82s/X/NrP1/wqI7v8KiO7/Bmvr/wZr6/8Ga+v/Dku6/w5Luv8OS7r/Fj+T8xY/k/MAAAAkAAAAJAAAACQuabahLmm2oS5ptqE1es7/NXrO/0a/+/9Gv/v/Rr/7/2LW9v9i1vb/Ytb2/2vc9f9r3PX/dN31/3Td9f903fX/e974/3ve+P973vj/X9T9/1/U/f9Z0Pz/WdD8/1nQ/P9Uyfv/VMn7/1TJ+/9Sv/j/Ur/4/4XP+v+Fz/r/hc/6/9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///J8f7/yfH+/8nx/v+Hyfn/h8n5/1Ow9v9TsPb/U7D2/1G29/9Rtvf/Ubb3/1K79/9Su/f/Ur34/1K9+P9Svfj/Urz4/1K8+P9SvPj/Urn3/1K59/9Stff/UrX3/1K19/99yfj/fcn4/33J+P/B7v3/we79/9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fn//9X5//94yfn/eMn5/3jJ+f9Sv/n/Ur/5/1K/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///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6//+o4/z/qOP8/6jj/P9cw/j/XMP4/13N+v9dzfr/Xc36/17V/P9e1fz/XtX8/1/Y/f9f2P3/X9r9/1/a/f9f2v3/X9j8/1/Y/P9f2Pz/Xtf7/17X+/9e1fr/XtX6/17V+v8kt/b/JLf2/yS39v8QnPL/EJzy/wp87/8KfO//Cnzv/xFNs/8RTbP/EU2z/xU9jt0VPY7dAAAAGgAAABoAAAAaJVKLiSVSi4klUouJN3vP/zd7z/9d0Pv/XdD7/13Q+/9t2/j/bdv4/23b+P+I4vb/iOL2/57n9/+e5/f/nuf3/7Ts+P+07Pj/tOz4/6Xp+/+l6fv/Ztz9/2bc/f9m3P3/YNb8/2DW/P9g1vz/Xc36/13N+v9ixPj/YsT4/2LE+P/U+f//1Pn//9T5///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//9X6///V+v//1fr//6jj/P+o4/z/qOP8/1zD+P9cw/j/Xc36/13N+v9dzfr/XtX8/17V/P9e1fz/X9j9/1/Y/f9f2v3/X9r9/1/a/f9f2Pz/X9j8/1/Y/P9e1/v/Xtf7/17V+v9e1fr/XtX6/yS39v8kt/b/JLf2/xCc8v8QnPL/Cnzv/wp87/8KfO//EU2z/xFNs/8RTbP/FT2O3RU9jt0AAAAaAAAAGgAAABouZJxeLmScXi5knF43fNH/N3zR/2HJ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///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//8Lx/v/C8f7/wvH+/4XW+v+F1vr/Zc35/2XN+f9lzfn/ZtX7/2bV+/9m1fv/Z9z8/2fc/P9o4P3/aOD9/2jg/f9q4v3/auL9/2ri/f9q4v7/auL+/2nj/v9p4/7/aeP+/2ji/f9o4v3/aOL9/2jg/f9o4P3/TNf7/0zX+/9M1/v/Gb73/xm+9/8Zvvf/E6f1/xOn9f8Nf+r/DX/q/w1/6v8XQZf/F0GX/xdBl/8LIUyHCyFMhwMRJAwDESQMAxEkDD2ExSI9hMUiPYTFIjl/0/85f9P/W7br/1u26/9btuv/e+L8/3vi/P974vz/uu35/7rt+f/Q8vr/0PL6/9Dy+v/j9/v/4/f7/+P3+//x+vv/8fr7/932/P/d9vz/3fb8/3Xi/f914v3/deL9/2rc/P9q3Pz/Z9T7/2fU+/9n1Pv/te3+/7Xt/v+17f7/t+39/7ft/f9oxfj/aMX4/2jF+P9/z/n/f8/5/3/P+f/B8P3/wfD9/9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//1Pr//9T6///U+v//wvH+/8Lx/v/C8f7/hdb6/4XW+v9lzfn/Zc35/2XN+f9m1fv/ZtX7/2bV+/9n3Pz/Z9z8/2jg/f9o4P3/aOD9/2ri/f9q4v3/auL9/2ri/v9q4v7/aeP+/2nj/v9p4/7/aOL9/2ji/f9o4v3/aOD9/2jg/f9M1/v/TNf7/0zX+/8Zvvf/Gb73/xm+9/8Tp/X/E6f1/w1/6v8Nf+r/DX/q/xdBl/8XQZf/F0GX/wshTIcLIUyHAxEkDAMRJAwDESQMPYTFIj2ExSI9hMUiOX/T/zl/0/9btuv/W7br/1u26/974vz/e+L8/3vi/P+67fn/uu35/9Dy+v/Q8vr/0PL6/+P3+//j9/v/4/f7//H6+//x+vv/3fb8/932/P/d9vz/deL9/3Xi/f914v3/atz8/2rc/P9n1Pv/Z9T7/2fU+/+17f7/te3+/7Xt/v+37f3/t+39/2jF+P9oxfj/aMX4/3/P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AB/4AAAAAP///////wAAAAAf+AAAAAD//////+AAAAAAAAAAAAAAB//////gAAAAAAAAAAAAAAf/////4AAAAAAAAAAAAAAH////+AAAAAAAAAAAAAAAAP////gAAAAAAAAAAAAAAAD////gAAAAAAAAAAAAAAAAH///4AAAAAAAAAAAAAAAAB///+AAAAAAAAAAAAAAAAAf///gAAAAAAAAAAAAAAAAB///4AAAAAAAAAAAAAAAAAf//+AAAAAAAAAAAAAAAAAH//8AAAAAAAAAAAAAAAAAAP//AAAAAAAAAAAAAAAAAAD/+AAAAAAAAAAAAAAAAAAA//gAAAAAAAAAAAAAAAAAAP/4AAAAAAAAAAAAAAAAAAD/+AAAAAAAAAAAAAAAAAAAH/gAAAAAAAAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAAAAf4AAAAAAAAAAAAAAAAAAAH+AAAAAAAAAAAAAAAAAAAB/gAAAAAAAAAAAAAAAAAAAf4AAAAAAAAAAAAAAAAAAAH+AAAAAAAAAAAAAAAAAAAB/gAAAAAAAAAAAAAAAAAAAH4AAAAAAAAAAAAAAAAAAAB+AAAAAAAAAAAAAAAAAAAAfgAAAAAAAAAAAAAAAAAAAH4AAAAAAAAAAAAAAAAAAABwAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAAAAAAAAAAABwAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAAAAAAAAAAABwAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAAAAAAAAAAABwAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAH4AAAAAAAAAAAAAAAAAAAB+AAAAAAAAAAAAAAAAAAAAfgAAAAAAAAAAAAAAAAAAAH4AAAAAAAAAAAAAAAAAAAH+AAAAAAAAAAAAAAAAAAAB/gAAAAAAAAAAAAAAAAAAAf4AAAAAAAAAAAAAAAAAAAH+AAAAAAAAAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAAAAf+AAAAAAAAAAAAAAAAAAAH/gAAAAAAAAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAAAD/+AAAAAAAAAAAAAAAAAAA//8AAAAAAAAAAAAAAAAAAP//AAAAAAAAAAAAAAAAAAD//wAAAAAAAAAAAAAAAAAA//8AAAAAAAAAAAAAAAAAAP//AAAAAAAAAAAAAAAAAAD//wAAAAAAAAAAAAAAAAAA//gAAAAAAAAAAAAAAAAAAP/4AAAAAAAAAAAAAAAAAAD/+AAAAAAAAAAAAAAAAAAAH/gAAAAAAAAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAAAAf4AAAAAAAAAAAAAAAAAAAH+AAAAAAAAAAAAAAAAAAAB/gAAAAAAAAAAAAAAAAAAAf4AAAAAAAAAAAAAAAAAAAH+AAAAAAAAAAAAAAAAAAAB/gAAAAAAAAAAAAAAAAAAAH4AAAAAAAAAAAAAAAAAAAB+AAAAAAAAAAAAAAAAAAAAfgAAAAAAAAAAAAAAAAAAAH4AAAAAAAAAAAAAAAAAAAB+AAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAAAAAAAAAAABwAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAAAAAAAAAAABwAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAHAAAAAAAAAAAAAAAAAAAABwAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAH4AAAAAAAAAAAAAAAAAAAB+AAAAAAAAAAAAAAAAAAAAfgAAAAAAAAAAAAAAAAAAAH4AAAAAAAAAAAAAAAAAAAB+AAAAAAAAAAAAAAAAAAAAfgAAAAAAAAAAAAAAAAAAAH4AAAAAAAAAAAAAAAAAAAH+AAAAAAAAAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAAAAf+AAAAAAAAAAAAAAAAAAAH/gAAAAAAAAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAAAD/+AAAAAAAAAAAAAAAAAAA//gAAAAAAAAAAAAAAAAAAP//AAAAAAAAAAAAAAAAAAD//wAAAAAAAAAAAAAAAAAA//8AAAAAAAAAAAAAAAAAB///AAAAAAAAAAAAAAAAAAf//wAAAAAAAAAAAAAAAAAH///gAAAAAAAAAAAAAAAAH///4AAAAAAAAAAAAAAAAB///+AAAAAAAAAAAAAAAAAf///4AAAAAAAAAAAAAAAA////+AAAAAAAAAAAAAAAAP////8AAAAAAAAAAAAAAAf/////AAAAAAAAAAAAAAAH/////wAAAAAAAAAAAAAAB//////4AAAAAB/gAAAAAB//////+AAAAAAf4AAAAAAf//////gAAAAAH+AAAAAAH///////4AAAB///AAAAH////////+AAAAf//wAAAB///////////x//////+P////////////8f//////j/////////////H//////4//////8="


#--------------------------------------------------import-----------------------------------------------------



from tkinter import messagebox,filedialog
import os
from threading import Thread
try:
    import win32gui
    import win32con
    import win32api
except ImportError:
    autoinstall("pywin32")
    import win32gui
    import win32con
    import win32api
import ctypes
from ctypes.wintypes import WPARAM,HHOOK
from ctypes import windll,wintypes
from tkinter import *
from tkinter.ttk import *
import tkinter
from time import sleep
from typing import Literal
import sys
import socket
from struct import pack
try:
    from pyautogui import position
except ImportError:
    autoinstall("pyautogui")
    from pyautogui import position
from re import findall
import win32process
try:
    from suspend import *
except ImportError:
    print("Error when importing suspend.py, copying and createing...")
    suspend_module = '''import psutil
from threading import Thread


def get_process_pid(process_name):
    """
    根据进程名获取进程的 PID
    :param process_name: 进程名
    :return: 进程的 PID 列表
    """
    pids = []
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            pids.append(proc.pid)
    return pids


def suspend_process(program):
    if not program:
        return -1
    if isinstance(program,int):
        pid = program
    elif isinstance(program,list):
        pid = program[0]
        if len(program)>1:
            for i in program[1:]:
                Thread(target=lambda:suspend_process(i)).start()
    else:
        pids = get_process_pid(program)
        pid = pids[0]
        if len(program)>1:
            for i in pids[1:]:
                Thread(target=lambda:suspend_process(i)).start()
    """
    挂起指定 PID 的进程
    :param pid: 进程的 PID
    """
    try:
        process = psutil.Process(pid)
        process.suspend()
        print(f"进程 {pid} 已挂起")
    except psutil.NoSuchProcess:
        print(f"错误: 进程 {pid} 不存在")
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")


def resume_process(program):
    if not program:
        return -1
    if isinstance(program,int):
        pid = program
    elif isinstance(program,list):
        pid = program[0]
        if len(program)>1:
            for i in program[1:]:
                Thread(target=lambda:resume_process(i)).start()
    else:
        pids = get_process_pid(program)
        pid = pids[0]
        if len(program)>1:
            for i in pids[1:]:
                Thread(target=lambda:resume_process(i)).start()
    ""
    """
    取消挂起指定 PID 的进程
    :param pid: 进程的 PID
    """
    try:
        process = psutil.Process(pid)
        process.resume()
        print(f"进程 {pid} 已恢复")
    except psutil.NoSuchProcess:
        print(f"错误: 进程 {pid} 不存在")
    except Exception as e:
        print(f"错误: 发生了一个未知错误: {e}")

if __name__ == "__main__":
    process_pid = get_process_pid("未命名1.exe")
    print(process_pid)
    input("按回车继续")
    suspend_process(process_pid)
    print("挂起")
    input("按回车继续")
    resume_process(process_pid)
    print("恢复")'''
    file = open("suspend.py","w",encoding="utf-8")
    file.write(suspend_module)
    file.close()
    print("suspend.py created successfully")
    try:
        from suspend import *
    except ImportError:
        autoinstall("psutil")
        from suspend import *
try:
    import easyStray
except ImportError:
    print("Error when importing easyStray.py, copying and createing...")
    easystray_module = '''from pystray import Icon, Menu, MenuItem
from PIL import Image
from threading import Thread

class Items:
    def __init__(self):
        self.items = []
    
    def add(self,text="",action=lambda:None,enabled=True):
        self.items.append(MenuItem(text,action,enabled=enabled))
    
    def get(self):
        return tuple(self.items)

    def clear(self):
        self.items = []

class StrayIcon:
    def __init__(self,items=(),hover_text="",icon="",exit_actions=lambda:None):
        self.hover_text = hover_text
        if not icon:
            raise ValueError("icon is empty")
        self.image = Image.open(icon)
        if isinstance(items,Items):
            items = items.get()
        items = items+(MenuItem("退出",self.stop,enabled=True),)
        self.icon = Icon("name",self.image,hover_text,items)
        self.exit_actions = exit_actions

    def run(self,asThread:bool=False):
        if asThread:
            Thread(target=self.icon.run,daemon=True).start()
        else:
            self.icon.run()

    def stop(self):
        self.icon.stop()
        self.exit_actions()

        
if __name__ == "__main__":
    icon = StrayIcon((),"我是程序","favicon.ico")
    icon.run()
        '''
    file = open("easyStray.py","w",encoding="utf-8")
    file.write(easystray_module)
    file.close()
    print("easyStray.py created successfully")
    try:
        import pystray
    except ImportError:
        autoinstall("pystray")
    else:
        del pystray
    import easyStray
from sys import argv
import sys
try:
    from date import Date
except ImportError:
    print("Error when importing date.py, copying and createing...")
    date_module = '''from time import *

class Date:
    def updateTime(self):
        self.time = localtime(time())

    def getsecond(self):
        self.updateTime()
        return self.time.tm_sec
    
    def getminute(self):
        self.updateTime()
        return self.time.tm_min
    
    def gethour(self):
        self.updateTime()
        return self.time.tm_hour
    
    def getday(self):
        self.updateTime()
        return self.time.tm_mday
    
    def getmonth(self):
        self.updateTime()
        return self.time.tm_mon
    
    def getyear(self):
        self.updateTime()
        return self.time.tm_year
    
    def getDayOfYear(self):
        self.updateTime()
        return self.time.tm_yday
    
    def getDayOfWeek(self):
        self.updateTime()
        return self.time.tm_wday

    def getFormatTime(self,format="%Y-%m-%d %H:%M:%S"):
        self.updateTime()
        return strftime(format,self.time)
    
if __name__ == "__main__":
    d = Date()
    print(d.getFormatTime())
'''
    file = open("date.py","w",encoding="utf-8")
    file.write(date_module)
    file.close()
    print("date.py created successfully")
    from date import Date
try:
    from argvParser import parse_arguments
except ImportError:
    print("Error when importing argvParser.py, copying and createing...")
    argv_parser_module = '''def parse_arguments(argv,valid_identifiers,return_type):
    """
    解析命令行参数。

    :param argv: 命令行参数列表。
    :param valid_identifiers: 有效的标识符列表，每个标识符由名称和参数数量组成。
    :param return_type: 返回类型，"list" 或 "dict"。
    :return: 解析后的参数列表，每个元素对应一个标识符。
    """
    args = argv[1:]
    result = [0] * len(valid_identifiers)
    i = 0
    while i < len(args):
        arg = args[i]
        found = False
        for j, (identifier, num_params) in enumerate(valid_identifiers):
            if arg == identifier:
                found = True
                if num_params == 0:
                    result[j] = 1
                elif num_params == 1:
                    if i + 1 < len(args):
                        result[j] = args[i + 1]
                        i += 1
                    else:
                        print(f"错误: 标识符 {identifier} 需要 1 个参数，但提供的参数不足。")
                        return None
                break
        if not found:
            print(f"错误: 未知的标识符 {arg}。")
            return None
        i += 1
    if return_type=="dict":
        result = {identifier: value for identifier, value in zip([i[0] for i in valid_identifiers], result)}
    return result
    
    
    '''
    file = open("argvParser.py","w",encoding="utf-8")
    file.write(argv_parser_module)
    file.close()
    print("argvParser.py created successfully")
    from argvParser import parse_arguments
from base64 import b64decode
from pyperclip import copy


#--------------------------------------------------import-----------------------------------------------------


TEMP_FOLDER = "Jiyu_tmp"
LOG_FOLDER = "log"


ARGV = argv[1:]
exit = sys.exit
#print = lambda string:messagebox.showinfo(title="控制台输出",message=string)
d = Date()
def logging(string:str):
    "[年-月-日 时:分:秒] 内容"
    
    logging_file.write("[%s] %s\n"%(d.getFormatTime("%Y-%m-%d %H:%M:%S"),string))

def print(string:str):
    sys.stdout.write(str(string)+"\n")
    sys.stdout.flush()
    if CONFIGS["--disableLogging"] or CONFIGS["/disableLogging"]:
        return 0
    logging(string)

JIYU_NAME = "StudentMain.exe"
taskmgr_opening = False
NULL = None
starting = False
windoweds = False
minisized = False
nohookthreadrunning = False
autoPauseing = False
CONFIGS = parse_arguments(argv, [
    ("--secret", 0), ("/secret", 0), 
    ("--autohide", 0), ("/autohide", 0),
    ("--autoStart", 0), ("/autoStart", 0),
    ("--help", 0),("-h",0),("/help", 0),("/h",0),("/?",0),
    ("--disableLogging",0),("/disableLogging",0),
    ("--version",0),("-v",0),("/version",0),("/v",0),
    ("--createLaunchScript",0),("/createLaunchScript",0),
    ("--moveToClose",0),("/moveToClose",0),
    ("--createShortcut",0),("/createShortcut",0),
    ("-f",0),("--no-flash",0),("/f",0),("/no-flash",0),
    ("--no-icon",0),("/no-icon",0),
    ("--stray",0),("/stray",0),
    ("--temp",1),("/temp",1),
    ("--log",1),("/log",1)
    ],
    "dict"
    )

if CONFIGS==None:
    exit()

if "temp" in CONFIGS.keys():
    TEMP_FOLDER = CONFIGS["temp"]
if "log" in CONFIGS.keys():
    LOG_FOLDER = CONFIGS["log"] 

if not os.path.exists(TEMP_FOLDER):
    os.mkdir(TEMP_FOLDER)#创建临时文件夹

if not os.path.exists(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)#创建临时文件夹

if ((not os.path.exists("favicon.ico")) or (not os.path.exists(TEMP_FOLDER+"/favicon.ico"))) and (not CONFIGS["--no-icon"]):
    file = open(TEMP_FOLDER+"/favicon.ico","wb")
    file.write(b64decode(ICON))
    file.close()

if not (CONFIGS["--disableLogging"] or CONFIGS["/disableLogging"]):
    logging_file = open(LOG_FOLDER+"/"+str(d.getFormatTime("%Y-%m-%d"))+".log","a",encoding="utf-8")
    sys.stderr = logging_file

if CONFIGS["--help"] or CONFIGS["-h"] or CONFIGS["/help"] or CONFIGS["/h"] or CONFIGS["/?"]:
    print(f"""
    JiyuKiller{VERSION}.py 帮助文档
    --secret 启动极域终结者时隐藏窗口
    --autohide 关闭极域终结者时隐藏窗口
    --autoStart 配置开机自启动
    -h --help 显示帮助文档
    --disableLogging 禁用日志
    -v --version 显示版本号
    --createLaunchScript 创建启动脚本
    --moveToClose 当鼠标移动到屏幕左上角时关闭程序
    --createShortcut 创建桌面快捷方式
    -f --no-flash 禁用启动时检测极域启动状态
    --no-icon 禁用窗口图标显示
    --stray 启用托盘图标。此选项可能会导致程序启动失败。必须与--autohide或--secret一起选择。
    """)
    exit()

if CONFIGS["--autoStart"] or CONFIGS["/autoStart"]:
    print(os.popen("schtasks /create /tn \"极域终结者\" /tr \"%s --secret\" /sc onstart"%os.path.abspath(__file__)).read())
    exit()

if CONFIGS["--version"] or CONFIGS["-v"] or CONFIGS["/version"] or CONFIGS["/v"]:
    print(f"JiyuKiller{VERSION}.py 版本号: {VERSION}\n{VERSION_PROMPT}")
    exit()

if CONFIGS["--createLaunchScript"] or CONFIGS["/createLaunchScript"]:
    file = open("launch.bat","w",encoding="utf-8")
    file.write("@echo off\n")
    a = argv
    a.remove("--createLaunchScript")
    file.write("python %s"%" ".join(a))
    del a
    print("Create launch script success.")
    exit()

if CONFIGS["--createShortcut"] or CONFIGS["/createShortcut"]:
    try:
        from createShortcut import create_desktop_shortcut
    except ImportError:
        create_shortcut_module = '''import winshell
import os


def create_desktop_shortcut(target_path, shortcut_name, description="", icon="",working_dir=None):
    """
    创建桌面快捷方式

    :param target_path: 目标文件或程序的路径
    :param shortcut_name: 快捷方式的名称
    :param description: 快捷方式的描述信息，默认为空字符串
    :param working_dir: 工作目录，默认为 None
    :return: 若创建成功返回 True，否则返回 False
    """
    try:
        # 获取桌面路径
        desktop_path = winshell.desktop()
        # 构建快捷方式的完整路径
        shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")

        # 创建快捷方式对象
        with winshell.shortcut(shortcut_path) as shortcut:
            # 设置目标路径
            shortcut.path = target_path
            # 设置描述信息
            shortcut.description = description
            if icon:
                # 设置图标路径（可选）
                shortcut.icon_location = icon
            if working_dir:
                # 设置工作目录
                shortcut.working_directory = working_dir
        return True
    except Exception as e:
        print(f"创建快捷方式时出错: {e}")
        return False
    '''
        file = open("createShortcut.py","w",encoding="utf-8")
        file.write(create_shortcut_module)
        file.close()
        try:
            from createShortcut import create_desktop_shortcut
        except ImportError:
            os.system("pip install winshell")
            from createShortcut import create_desktop_shortcut
    create_desktop_shortcut(os.path.abspath(__file__),"极域终结者4.0")
    exit()



x = 0
y = 0

def mainloop():
    global x,y
    global windoweds,minisized,nohookthreadrunning,autoPauseing
    while True:
        check_position()
        try:
            topmost_self()
        except:
            pass
        check_start_status()
        if window.get() == 1:
            if starting == True and windoweds == False:
                ban_broadcast()
                windoweds = True
        if mini.get() == 1:
            if starting == True and minisized == False:
                flash_window()
                minisize(mythwarehwnd)
                minisized = True
        if nohook.get() == 1:
            if starting == True and nohookthreadrunning == False:
                Thread(target=KeyHookThreadProc,daemon=True).start()
                nohookthreadrunning = True
        if autoPause.get()==1:
            if starting == True and autoPauseing==False:
                Thread(target=auto_pause_thread,daemon=True).start()
                autoPauseing = True
        sleep(0.1) #延时防卡顿

def check_position():
    x,y = position()
    pointer_pos.config(text=str(x)+","+str(y)+"   "+str(root.winfo_width())+"+"+str(root.winfo_height()))
    if int(x) == 0 and int(y) == 0 and move_to_close.get() == 1:
        messagebox.showinfo(title="控制台输出",message=os.popen("taskkill /im %s /f /t"%JIYU_NAME).read())
        flash()

def check_start_status():
    global starting,windoweds,minisized
    flash_window()
    if mythwarehwnd == NULL:
        starting = False
        windoweds = False
        minisized = False
    else:
        starting = True

def topmost_self(hwn=win32gui.FindWindow(None,u'极域终结者')):
    win32gui.SetWindowPos(hwn,win32con.HWND_TOPMOST,0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def destroy(hwnd=win32gui.GetForegroundWindow()):
    win32api.PostMessage(hwnd,win32con.WM_CLOSE,0,0)

def minisize(hwnd=win32gui.GetForegroundWindow()):
    win32gui.ShowWindow(hwnd,win32con.SW_MINIMIZE)

def windowed(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_COMMAND, WPARAM((win32con.BM_CLICK << 16) | 1004), NULL)

# 加载 user32.dll
windll = ctypes.windll.user32

# 定义 HookProc 函数
def HookProc(nCode, wParam, lParam):
    return False

LRESULT = ctypes.c_long
# 定义 HOOKPROC 函数类型
HOOKPROC = ctypes.WINFUNCTYPE(LRESULT, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)

# 定义 KeyHookThreadProc 函数
def KeyHookThreadProc():
    global nohookthreadrunning
    while nohook.get()==1:
        # 设置键盘钩子
        kbdHook = windll.SetWindowsHookEx(win32con.WH_KEYBOARD_LL, HOOKPROC(HookProc), win32api.GetModuleHandle(None), 0)
        # 等待 25 毫秒
        sleep(0.025)
        # 卸载键盘钩子
        windll.UnhookWindowsHookEx(kbdHook)
    nohookthreadrunning = False

def bottomed(hwnd):
    win32gui.SetWindowPos(mythwarehwnd, win32con.HWND_BOTTOM, 0, 0, 300, 300,win32con.SWP_NOMOVE | win32con.SWP_SHOWWINDOW)

def close_taskkill():
    lis = os.popen('tasklist /fi "imagename eq StudentMain.exe"').readlines()
    if len(lis) < 4:
        log("极域未运行")
        return 0
    messagebox.showinfo(title="控制台输出",message=os.popen("taskkill /im %s /f /t"%JIYU_NAME).read())
    flash()

def scan_starting():
    global JIYU_PID
    for i in os.popen("tasklist").read().split("\n"):
        if "StudentMain.exe" in i:
            JIYU_PID = get_process_pid(JIYU_NAME)
            print("Get pid successfully")
            return True
    return False

def flash():
    root.bell()
    l.config(text="刷新中...")
    s = scan_starting()
    l.config(text="运行中" if s else "不在运行",fg="green" if s else "red")


def flash_window():
    global mythwarehwnd
    mythwarehwnd = win32gui.FindWindow(None, '屏幕广播')  # 使用窗口标题查找窗口句柄

def auto_pause_thread():
    global autoPauseing
    while autoPause.get()==1:
        searchJiyu()
        suspend_process(JIYU_PID)
        print("Suspend process")
        sleep(10)
        resume_process(JIYU_PID)
        print("Resume process")
    autoPauseing = False

def searchJiyu():
    global JIYU_PID
    JIYU_PID = get_process_pid(JIYU_NAME)

def runFuncAsThread(func):
    Thread(target=func,daemon=True).start()

def showRoot():
    root.deiconify()

def whenRootClose():
    root.withdraw()

def whenProgramClose():
    root.destroy()
    logging_file.close()

def log(prompt:str):
    logging_label.config(text=prompt)

def ntsd(system_version:Literal["win7","win10"]):
    searchJiyu()
    log(os.popen("ntsd-"+system_version+".exe -c q -p "+str(JIYU_PID)).read())

def copyLog():
    copy(l["text"])
    root.bell()

def getIp():
    import traceback
    try:
        print("getip")
        ips = []
        if os.path.exists("ips"):
            print("has")
            f = open("ips","r",encoding="utf-8")
            ips = f.readlines()
            f.close()
            del f
        ips = ["224.50.50.42"]+ips
        #print(ips)
        print("geted")
        return tuple(ips)
    except:
        print(traceback.format_exc())



def ban_broadcast():
    # Define constants and variables
    control_id = 1004
    main_window_handle = None
    child_window_handles = []
    target_child_handle = None
    control_handle = None
    is_button_disabled = False
    button_rect = (0, 0, 0, 0)
    button_x = 0
    button_y = 0

    # Wait for "屏幕广播" window to appear
    while True:
        main_window_handle = win32gui.FindWindow(None, "屏幕广播")
        if main_window_handle != 0:
            break
        # Add a delay to avoid excessive polling
        win32api.Sleep(500)

    # Enumerate child windows
    def enum_windows_proc(hwnd, lParam):
        child_window_handles.append(hwnd)
        return True
    win32gui.EnumChildWindows(main_window_handle, enum_windows_proc, None)

    # Find child window with class name "AfxWnd80u"
    target_child_handle = None
    for hwnd in child_window_handles:
        class_name = win32gui.GetClassName(hwnd)
        if class_name == "AfxWnd80u":
            target_child_handle = hwnd
            break

    if target_child_handle is None:
        print("未找到缩放按钮")
        return

    # Get control handle
    control_handle = win32gui.GetDlgItem(target_child_handle, control_id)
    if control_handle == 0:
        print("获取缩放按钮对象失败")
        return

    # Check if button is disabled
    is_button_enabled = win32gui.IsWindowEnabled(control_handle)
    if not is_button_enabled:
        print("缩放按钮当前禁用")
    else:
        print("缩放按钮当前启用")

    # If button is disabled, enable it
    if not is_button_enabled:
        # Enable the button if it's disabled
        win32gui.EnableWindow(control_handle, True)
        print("缩放按钮启用成功")

    # Get button coordinates
    button_rect = win32gui.GetWindowRect(control_handle)
    button_x = button_rect[0]
    button_y = button_rect[1]

    # Simulate mouse click
    win32api.SetCursorPos((button_x, button_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    # Set window to normal (windowed) mode
    win32gui.ShowWindow(main_window_handle, win32con.SW_RESTORE)  # Restores window to normal size

    


# 原始数据模板（省略部分重复内容，保持原结构）
store = [[0x44, 0x4d, 0x4f, 0x43, 0x00, 0x00, 0x01, 0x00, 0x9e, 0x03, 0x00, 0x00, 0x10, 0x41, 0xaf, 0xfb, 0xa0, 0xe7, 0x52, 0x40, 0x91, 
          0xdc, 0x27, 0xa3, 0xb6, 0xf9, 0x29, 0x2e, 0x20, 0x4e, 0x00, 0x00, 0xc0, 0xa8, 0x50, 0x81, 0x91, 0x03, 0x00, 0x00, 0x91, 0x03, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
         [0x44, 0x4d, 0x4f, 0x43, 0x00, 0x00, 0x01, 0x00, 0x6e, 0x03, 0x00, 0x00, 0x39, 0x8e, 0xd2, 0x7c, 0x8b, 0x56, 0x0d, 0x45, 0x9c, 0x60, 0xe0, 0xd0, 0xc4, 0xa4, 0xb3, 0xf2, 0x20, 0x4e, 0x00, 0x00, 0xc0, 0xa8, 0x50, 0x81, 0x61, 0x03, 0x00, 0x00, 0x61, 0x03, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x43, 0x00, 0x3a, 0x00, 0x5c, 0x00, 0x57, 0x00, 0x69, 0x00, 0x6e, 0x00, 0x64, 0x00, 0x6f, 0x00, 0x77, 0x00, 0x73, 0x00, 0x5c, 0x00, 0x73, 0x00, 0x79, 0x00, 0x73, 0x00, 0x74, 0x00, 0x65, 0x00, 0x6d, 0x00, 0x33, 0x00, 0x32, 0x00, 0x5c, 0x00,
             0x63, 0x00, 0x6d, 0x00, 0x64, 0x00, 0x2e, 0x00, 0x65, 0x00, 0x78, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
         [0x44, 0x4d, 0x4f, 0x43, 0x00, 0x00, 0x01, 0x00, 0x2a, 0x02, 0x00, 0x00, 0xbf, 0x40, 0x22, 0x4e, 0x57, 0x2d, 0x3e, 0x4f, 0x9b, 0x6f, 0xc1, 0x8d, 0xe1, 0xeb, 0x4f, 0x62, 0x20, 0x4e, 0x00, 0x00, 0xc0, 0xa8, 0x50, 0x81, 0x1d, 0x02, 0x00, 0x00, 0x1d, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x13, 0x00, 0x00, 0x10, 0x0f, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x59, 0x65, 0x08, 0x5e, 0x06, 0x5c, 0xcd, 0x91, 0x2f, 0x54, 0xa8, 0x60, 0x84, 0x76, 0xa1, 0x8b, 0x97, 0x7b, 0x3a, 0x67, 0x02, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
         [0x44, 0x4d, 0x4f, 0x43, 0x00, 0x00, 0x01, 0x00, 0x2a, 0x02, 0x00, 0x00, 0xc8, 0xe3, 0x97, 0xfd, 0xc0, 0xb5, 0x9f, 0x45, 0x87, 0x72, 0x05, 0xbd, 0x4e, 0x46, 0xa8, 0x96, 0x20, 0x4e, 0x00, 0x00, 0xc0, 0xa8, 0x50, 0x81, 0x1d, 0x02, 0x00, 0x00, 0x1d, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 0x00, 0x10, 0x0f, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x59, 0x65, 0x08, 0x5e, 0x06, 0x5c, 0x73, 0x51, 0xed, 0x95, 0xa8, 0x60, 0x84, 0x76, 0xa1, 0x8b, 0x97, 0x7b, 0x3a, 0x67, 0x02, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]]

basicCMD = {
    '-msg': store[0],
    '-c': store[1],
    '-r': store[2],
    '-s': store[3],
}

# 格式化内容为16进制数组
def format_b4_send(content):
    arr = []
    for ch in content:
        # 处理字符为高低位字节（原逻辑实现）
        char_code = ord(ch)
        low = char_code & 0xFF  # 低位字节
        high = (char_code >> 8) & 0xFF  # 高位字节
        arr.append(low)
        arr.append(high)
    return arr

# 发送UDP数据包的基础函数
def send_udp_packet(target_ip, port, packet):
    try:
        # 转换16进制数组为二进制流
        payload = pack(f"{len(packet)}B", *packet)
        # 创建UDP套接字并发送
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(payload, (target_ip, port))
        return True
    except Exception as e:
        print(f"发送失败: {e}")
        return False

# 1. 发送消息
def send_message(target_ip, port, message, loop=1, interval=22):
    """发送消息数据包
    :param target_ip: 目标IP
    :param port: 目标端口
    :param message: 要发送的消息内容
    :param loop: 循环次数
    :param interval: 循环间隔（秒）
    """
    for _ in range(loop):
        # 复制消息模板并填充内容
        packet = basicCMD['-msg'].copy()
        formatted_content = format_b4_send(message)
        # 填充内容到模板（假设从索引100开始，根据原逻辑调整）
        for i, val in enumerate(formatted_content):
            if 100 + i < len(packet):  # 防止数组越界
                packet[100 + i] = val
        # 发送数据包
        send_udp_packet(target_ip, port, packet)
        if _ < loop - 1:
            import time
            time.sleep(interval)
    print(f"消息发送完成（{loop}次）")

# 2. 执行命令
def execute_command(target_ip, port, command, loop=1, interval=22):
    """发送执行命令数据包
    :param target_ip: 目标IP
    :param port: 目标端口
    :param command: 要执行的命令（如"cmd.exe /c ipconfig"）
    :param loop: 循环次数
    :param interval: 循环间隔（秒）
    """
    for _ in range(loop):
        # 复制命令模板并填充内容
        packet = basicCMD['-c'].copy()
        formatted_cmd = format_b4_send(command)
        # 填充命令到模板（原逻辑从索引100开始）
        for i, val in enumerate(formatted_cmd):
            if 100 + i < len(packet):
                packet[100 + i] = val
        # 发送数据包
        send_udp_packet(target_ip, port, packet)
        if _ < loop - 1:
            import time
            time.sleep(interval)
    print(f"命令执行包发送完成（{loop}次）")

# 3. 发送关机指令
def send_shutdown(target_ip, port, loop=1, interval=22):
    """发送关机数据包
    :param target_ip: 目标IP
    :param port: 目标端口
    :param loop: 循环次数
    :param interval: 循环间隔（秒）
    """
    for _ in range(loop):
        # 直接使用预设的关机模板
        packet = basicCMD['-s'].copy()
        send_udp_packet(target_ip, port, packet)
        if _ < loop - 1:
            import time
            time.sleep(interval)
    print(f"关机指令发送完成（{loop}次）")

# 4. 发送重启指令
def send_restart(target_ip, port, loop=1, interval=22):
    """发送重启数据包
    :param target_ip: 目标IP
    :param port: 目标端口
    :param loop: 循环次数
    :param interval: 循环间隔（秒）
    """
    for _ in range(loop):
        # 直接使用预设的重启模板
        packet = basicCMD['-r'].copy()
        send_udp_packet(target_ip, port, packet)
        if _ < loop - 1:
            import time
            time.sleep(interval)
    print(f"重启指令发送完成（{loop}次）")
    



if CONFIGS["--disableLogging"] or CONFIGS["/disableLogging"]:
    print("Disable logging")
if not (CONFIGS["--no-flash"] or CONFIGS["/no-flash"]):
    JIYU_PID = get_process_pid(JIYU_NAME)
    JIYU_PORT = 4705
    if not JIYU_PID:
        print("Get pid failed")
    else:
        print("Get pid successfully")
mythwarehwnd = win32gui.FindWindow(None, '屏幕广播')  # 使用窗口标题查找窗口句柄
root = Tk()
print("window seted.")
if CONFIGS["--autohide"] or CONFIGS["/autohide"]:
    print("hide window when close")
    root.protocol("WM_DELETE_WINDOW", whenRootClose)
if CONFIGS["--stray"] or CONFIGS["/stray"]:
    i = easyStray.Items()
    i.add(f"免费内测版本{VERSION}，作者：张泊桥",lambda:None,enabled=False)
    i.add("杀死极域", lambda: os.popen("taskkill /f /im StudentMain.exe"))
    if CONFIGS["--autohide"] or CONFIGS["--secret"] or CONFIGS["/autohide"] or CONFIGS["/secret"]:
        i.add("显示窗口", showRoot)
    icon = easyStray.StrayIcon(i,VERSION_PROMPT,"favicon.ico",whenProgramClose)
    icon.run(True)
print("stray created.")
window = IntVar()
mini = IntVar()
nohook = IntVar()
move_to_close = IntVar()
if CONFIGS["--moveToClose"] or CONFIGS["/moveToClose"]:
    print("Move to close on")
    move_to_close.set(1)
autoPause = IntVar()
if CONFIGS["--secret"] or CONFIGS["/secret"]:
    print("Secret mode on")
    root.withdraw()
root.title(f"Jiyu Killer{VERSION} Version")
if not (CONFIGS["--no-icon"] or CONFIGS["/no-icon"]):
    if os.path.exists("favicon.ico"):
        root.iconbitmap("favicon.ico")
    else:
        root.iconbitmap(TEMP_FOLDER+"/favicon.ico")


'''
root.attributes('-topmost', 'true')
root.resizable(False,False)
root.geometry("500x400")
l = tkinter.Label(root,text="未知，请刷新",fg="grey",font=("微软雅黑",15,"bold"))
l.pack()
l1 = tkinter.Label(root,text="",fg="grey",font=("微软雅黑",10,"bold"))
l1.pack()
print("creating component...")
Button(root,text="刷新启动状态 StudentMain.exe",command=lambda:runFuncAsThread(flash),width=40).pack()
Button(root,text="关闭 taskkill",command=close_taskkill,width=40).pack()
Button(root,text="刷新窗口进程 屏幕广播",command=flash_window,width=40).pack()
Button(root,text="最小化 屏幕广播",command=flash_window,width=40).pack()
Checkbutton(root,text="窗口化屏幕广播",variable=window,onvalue=1,offvalue=0).pack()
Checkbutton(root,text="最小化屏幕广播",variable=mini,onvalue=1,offvalue=0).pack()
Checkbutton(root,text="克制键盘锁",variable=nohook,onvalue=1,offvalue=0).pack()
Checkbutton(root,text="鼠标移到左上角以关闭",variable=move_to_close,onvalue=1,offvalue=0).pack()
Checkbutton(root,text="智能防控屏窥屏",variable=autoPause,onvalue=1,offvalue=0).pack()
Thread(target=mainloop,daemon=True).start()
check_position()
print("starting window...")
root.mainloop()
print("window started.")
'''
root.geometry("1000x400")
root.attributes("-topmost",1)
kill_jiyu_frame = Labelframe(root,text="杀死极域")
l = tkinter.Label(kill_jiyu_frame,text="未知，请刷新",fg="grey",font=("微软雅黑",15,"bold"))
l.place(relx=0.05,rely=0.05,relheight=0.2,relwidth=0.9)
l.bind("<Button-1>",lambda event:runFuncAsThread(flash))
Button(kill_jiyu_frame,text="taskkill杀",command=close_taskkill).place(relx=0.05,rely=0.283,relheight=0.2,relwidth=0.9)
Button(kill_jiyu_frame,text="win7-ntsd杀",command=lambda:ntsd("win7")).place(relx=0.05,rely=0.516,relheight=0.2,relwidth=0.9)
Button(kill_jiyu_frame,text="win10-ntsd杀",command=lambda:ntsd("win10")).place(relx=0.05,rely=0.749,relheight=0.2,relwidth=0.9)
kill_jiyu_frame.place(relx=0.025,rely=0,relheight=0.8,relwidth=0.3)
settings_frame = Labelframe(root,text="选项")
Checkbutton(settings_frame,text="克制键盘锁",variable=nohook,onvalue=1,offvalue=0).pack()
Checkbutton(settings_frame,text="鼠标移到左上角以关闭",variable=move_to_close,onvalue=1,offvalue=0).pack()
Checkbutton(settings_frame,text="智能防控屏窥屏",variable=autoPause,onvalue=1,offvalue=0).pack()
# Checkbutton(settings_frame,text="窗口化屏幕广播（Beta）",variable=window,onvalue=1,offvalue=0).pack()
settings_frame.place(relx=0.325,rely=0,relheight=0.8,relwidth=0.3)
broadcast_frame = Labelframe(root,text="屏幕广播")
broadcast_windowed = BooleanVar()
Checkbutton(broadcast_frame,text="窗口化",variable=broadcast_windowed,onvalue=1,offvalue=0).pack()
broadcast_hide = BooleanVar()
Checkbutton(broadcast_frame,text="隐藏",variable=broadcast_hide,onvalue=1,offvalue=0).pack()
control_frame = LabelFrame(root,text="反控")
atk_ip_address = Combobox(control_frame,values=getIp())
atk_ip_address.place(relx=0.1,rely=0.08,relwidth=0.8,relheight=0.12)
message = Entry(control_frame)
message.place(relx=0.1,rely=0.25,relwidth=0.5,relheight=0.12)
Button(control_frame,text="发送信息",command=lambda:send_message(atk_ip_address.get(),JIYU_PORT,message.get())).place(relx=0.65,rely=0.25,relwidth=0.25,relheight=0.12)
command = Entry(control_frame)
command.place(relx=0.1,rely=0.42,relwidth=0.5,relheight=0.12)
Button(control_frame,text="执行命令",command=lambda:execute_command(atk_ip_address.get(),JIYU_PORT,command.get())).place(relx=0.65,rely=0.42,relwidth=0.25,relheight=0.12)
Button(control_frame,text="关机",command=lambda:send_shutdown(atk_ip_address.get(),JIYU_PORT)).place(relx=0.1,rely=0.59,relwidth=0.8,relheight=0.12)
Button(control_frame,text="重启",command=lambda:send_restart(atk_ip_address.get(),JIYU_PORT)).place(relx=0.1,rely=0.76,relwidth=0.8,relheight=0.12)
control_frame.place(relx=0.625,rely=0,relheight=0.8,relwidth=0.375)
logging_label = tkinter.Label(root,text="Log输出123456abcdefg",font=("微软雅黑",10))
logging_label.place(relx=0.05,rely=0.82,relheight=0.16,relwidth=0.4)
logging_label.bind("<Button-1>",lambda event:copyLog())
pointer_pos = tkinter.Label(root,text="",fg="grey",font=("微软雅黑",10,"bold"))
pointer_pos.place(relx=0.45,rely=0.82,relheight=0.16,relwidth=0.25)
tkinter.Label(root,text="JiyuKiller"+VERSION,fg="grey",font=("微软雅黑",10,"bold")).place(relx=0.7,rely=0.82,relheight=0.16,relwidth=0.25)
Thread(target=mainloop,daemon=True).start()
check_position()
root.mainloop()

'''
仅供学习，请勿恶作剧
张泊桥制作
Copyright©张泊桥,All rights reversed.
'''



