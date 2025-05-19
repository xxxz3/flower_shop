<template>
    <div class="container">

        <!--表格数据-->
        <div class="table">
            <el-button type="primary" class="btn" @click="dialogVisible = true">新 增</el-button>

            <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%">
                <el-table-column label="序号" width="70" type="index" :index="indexMethod"/>
                <el-table-column prop="username" label="创建人" width="150"/>

                <el-table-column prop="cover_url" label="轮播图" width="225">
                    <template #default="scope">
                        <el-image style="width: 200px; height: 100px"
                                  :src="scope.row.image"></el-image>

                    </template>
                </el-table-column>

                <el-table-column prop="create_time" label="创建时间" width="200"/>

                <el-table-column label="操作" width="140">
                    <template #default="scope">
                        <el-button type="danger" @click="deleteBanner(scope.row)" size="small">删除</el-button>
                    </template>
                </el-table-column>

            </el-table>


            <!-- 页码展示-->
            <div style="margin-top: 20px">

                <el-pagination
                        :current-page="currentPage"
                        :page-size="pageSize"
                        :page-sizes="[10, 20, 30, 40,50]"
                        background
                        layout="total,sizes, prev, pager, next"
                        :total="tableData.length"
                        @size-change="handleSizeChange"
                        @current-change="handleCurrentChange"
                />
            </div>
        </div>

    </div>


  <!--  添加轮播图-->
    <el-dialog
            v-model="dialogVisible"
            title="添加轮播图"
            width="500"
    >
        <template #footer>
            <div class="dialog-footer">
                <el-form
                        ref="ruleFormRef"
                        style="max-width: 600px"
                        label-width="auto">

                    <div class="btn-addFlower">
                        <span style="color: #606266;font-size: 14px; margin-left: 15px;">鲜花图片</span>
                        <input type="file" style="margin-left: 12px" @change="flowerChange">
                        <img :src="previewImg" alt="" id="preview" title="预览图"/>
                    </div>

                </el-form>
                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="addBanner">
                    确定
                </el-button>
            </div>
        </template>
    </el-dialog>

</template>

<script setup>
import {ref, onMounted} from "vue";
import {ElMessage} from "element-plus";
import {addBannerRequest, deleteBannerRequest, getBannerRequest} from "@/apis/banner.js";
import usePage from "@/hooks/usePage.js";

const previewImg = ref('')  // 预览图
const tableData = ref([])  // 表格数据
const {
    pageSize,
    currentPage,
    handleSizeChange,
    handleCurrentChange,
    indexMethod
} = usePage()  // 分页
const dialogVisible = ref(false)  // 弹出框


// 发送请求获取轮播图列表
async function getBannerList() {
    const res = await getBannerRequest()
    tableData.value = res
    console.log(res)
}
onMounted(() => getBannerList())

// 删除逻辑
async function deleteBanner(row) {
    await deleteBannerRequest(row.id)
    getBannerList()
    ElMessage({
        type: "success",
        message: '删除成功'
    })
}

// 新增轮播图弹框确定按钮
async function addBanner() {
    const res = await addBannerRequest({
        image: previewImg.value,
    })
    ElMessage({
        type: "success",
        message: "轮播图添加成功！！！"
    })
    dialogVisible.value = false
    getBannerList()

}

// 读取图片信息
async function flowerChange(e) {
    const file = e.target.files[0];
    // 创建文件读取器
    const reader = new FileReader();
    reader.onload = e => {
        const dataUrl = e.target.result
        previewImg.value = dataUrl
    }
    // 以DataUrl格式读取文件
    reader.readAsDataURL(file);
}

</script>

<style scoped>


.btn {
    margin-bottom: 20px;
}

.avatar-uploader .avatar {
    width: 150px;
    height: 150px;
    display: block;
}
</style>

<style>
.avatar-uploader .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
    border-color: var(--el-color-primary);
}


.block .demonstration {
    display: block;
    color: var(--el-text-color-secondary);
    font-size: 14px;
    margin-bottom: 20px;
}

</style>