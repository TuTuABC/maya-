# -*- coding: utf-8 -*-
import multiprocessing


#初始化
def initialize():
    try:
        import maya.standalone
        maya.standalone.initialize(name="python")

    except:
        pass


#卸载
def uninitialize():
    try:
        import  maya.standalone
        maya.standalone.uninitialize()
    except:
        pass



#保存
def savefile():
    import  maya.cmds as mc
    try:
        mc.file(save=True,f = True)
    except:
        pass



#保存
def main(msg):
    import maya.cmds as mc
    try:
        mc.file(r"D:\ZXFY\scenes\render\v1\CJ\1920_1080/"+msg,open = True,f = True,options = "v=0",ignoreVersion = True)
        #修改vray的分辨率
        if mc.getAttr("defaultRenderGlobals.ren") == "vray":
            mc.setAttr("vraySettings.wi",1920)
            mc.setAttr("vraySettings.he", 1080)
            if mc.getAttr("vraySettings.pmt") == 3.0:
                mc.setAttr("vraySettings.pmt",6)
                if len(mc.ls("vrayRE_Denoiser")) == 0:
                    denoiser = mc.createNode("VRayRenderElement", n="vrayRE_Denoiser")
                    mc.addAttr(denoiser, ci=True, sn="vrayClassType", ln="vrayClassType", dt="string")
                    mc.addAttr(denoiser, ci=True, k=True, sn="enabled", ln="enabled", dv=1, min=0, max=1, at="bool")
                    mc.addAttr(denoiser, ci=True, k=True, sn="enableDeepOutput", ln="enableDeepOutput", dv=1, min=0,
                               max=1, at="bool")
                    mc.addAttr(denoiser, ci=True, sn="vray_alias_denoiser", ln="vray_alias_denoiser", dv=144, at="long")
                    mc.addAttr(denoiser, ci=True, sn="vray_name_denoiser", ln="vray_name_denoiser", dt="string")
                    mc.addAttr(denoiser, ci=True, sn="vray_mode_denoiser", ln="vray_mode_denoiser", dv=2, at="long")
                    mc.addAttr(denoiser, ci=True, sn="vray_engine_denoiser", ln="vray_engine_denoiser", at="long")
                    mc.addAttr(denoiser, ci=True, sn="vray_engine_denoiser_ipr", ln="vray_engine_denoiser_ipr", dv=1,
                               at="long")
                    mc.addAttr(denoiser, ci=True, sn="vray_preset_denoiser", ln="vray_preset_denoiser", dv=1, at="long")
                    mc.addAttr(denoiser, ci=True, sn="vray_strength_denoiser", ln="vray_strength_denoiser", dv=1, min=0,
                               smn=0.10000000149011612, smx=10, at="float")
                    mc.addAttr(denoiser, ci=True, sn="vray_radius_denoiser", ln="vray_radius_denoiser", dv=10, min=0,
                               smn=0.0099999997764825821, smx=50, at="float")
                    mc.addAttr(denoiser, ci=True, sn="vray_hardware_accel_denoiser", ln="vray_hardware_accel_denoiser",
                               dv=1, at="long")
                    mc.addAttr(denoiser, ci=True, sn="vray_generate_render_elements",
                               ln="vray_generate_render_elements", dv=1, at="long")
                    mc.addAttr(denoiser, ci=True, sn="vray_force_refresh_denoiser", ln="vray_force_refresh_denoiser",
                               dt="string")
                    mc.setAttr(denoiser + ".vrayClassType", "denoiserChannel", type="string")
                    mc.setAttr(denoiser + ".vray_name_denoiser", "denoiser", type="string")
                    mc.setAttr(denoiser + ".vray_engine_denoiser_ipr", 0)
                    mc.setAttr(denoiser + ".vray_force_refresh_denoiser", "vrayOnRefreshDenoiserPressed", type="string")

        if mc.getAttr("defaultRenderGlobals.ren") == "mayaSoftware":
            mc.setAttr("defaultResolution.w",1920)
            mc.setAttr("defaultResolution.h", 1080)
    except:
        pass

#这里定义子进程的内容
def func(msg):
    #先进行初始化
    initialize()
    if msg.endswith(".ma") or msg.endswith(".mb"):
        main(msg)
        savefile()
    #因为是批量任务，中途不需要卸载，否则导致失败
    #uninitialize()



if __name__ == "__main__":
    #多进程来加快处理速度
    import multiprocessing
    import os
    #使用进程池，设定最大同时运行15个进程，具体可以看着自己的线程数量和运行内存来
    pool = multiprocessing.Pool(processes=15)
    for i in os.listdir(r"D:\ZXFY\scenes\render\v1\CJ\1920_1080"):
        pool.apply_async(func,(i,))
    pool.close()
    pool.join()

