<template>
    <div class="container">
<div class="nav">
        <!-- 搜索-->
        <div class="input_search">
            <el-input v-model="input" style="width: 240px; margin-right: 20px" placeholder="输入公告标题查询">
                <template #prefix>
                    <el-icon class="el-input__icon">
                        <search/>
                    </el-icon>
                </template>
                <template #append>
                    <el-button @click="searchAnnouncement">查 询</el-button>
                </template>
            </el-input>


        </div>
        <div class="add_btn">
            <el-button type="primary" class="btn" @click="dialogVisible = true">新 增</el-button>
        </div>
</div>
        <!--表格数据-->
        <div class="table">

            <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%">
                <el-table-column label="序号" width="75" type="index" :index="indexMethod"/>
                <el-table-column prop="username" label="创建者" width="180"/>
                <el-table-column prop="title" label="公告标题" width="180"/>
                <el-table-column prop="content" label="公告内容" width="420" show-overflow-tooltip/>
                <el-table-column prop="create_time" label="创建时间" width="200"/>

                <el-table-column label="操作" width="140">
                    <template #default="scope">
                        <el-button type="danger" @click="deleteAnnouncement(scope.row)" size="small">删除</el-button>
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


    <el-dialog
            v-model="dialogVisible"
            title="添加公告"
            width="500"
    >
        <template #footer>
            <div class="dialog-footer">
                <el-form
                        ref="ruleFormRef"
                        style="max-width: 600px"
                        :model="Announcement"
                        label-width="auto">
                    <el-form-item label="标题" prop="title">
                        <el-input v-model="Announcement.title"/>
                    </el-form-item>

                    <el-form-item label="内容" prop="content">
                        <el-input v-model="Announcement.content"/>
                    </el-form-item>
                </el-form>
                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="addAnnouncement">
                    确定
                </el-button>
            </div>
        </template>
    </el-dialog>

</template>

<script setup>
import {ref, onMounted, reactive} from "vue";
import {Search} from '@element-plus/icons-vue'
import {ElMessage} from "element-plus";
import {addAnnouncementRequest, deleteAnnouncementRequest, getAnnouncementRequest} from "@/apis/announcement.js";
import useRole from "@/hooks/useRole.js";
import usePage from "@/hooks/usePage.js";


const Announcement = reactive({title: '', content: ''})  // 添加公告表单
const input = ref('')  // 查询输入框
const tableData = ref([])  // 表格数据
const {
    pageSize,
    currentPage,
    handleSizeChange,
    handleCurrentChange,
    indexMethod
} = usePage()  // 分页
const {role} = useRole()  // 获取当前登录的角色信息
const dialogVisible = ref(false)  // 弹出框


// 发送请求获取公告列表
async function getAnnouncementList() {
    const res = await getAnnouncementRequest()
    tableData.value = res
}

onMounted(() => getAnnouncementList())


const user_id = localStorage.getItem('user_id')


// 查询功能
async function searchAnnouncement() {
    const res = await getAnnouncementRequest(input.value)
    tableData.value = res
}


// 删除逻辑
async function deleteAnnouncement(row) {
    await deleteAnnouncementRequest(row.id)
    getAnnouncementList()
    ElMessage({
        type: "success",
        message: '删除成功'
    })
}

// 新增公告弹框确定按钮
async function addAnnouncement() {

        const res = await addAnnouncementRequest({
            title: Announcement.title,
            content: Announcement.content,
        })
        ElMessage({
            type: "success",
            message: "公告添加成功！！！"
        })
        getAnnouncementList()
        dialogVisible.value = false



}

</script>

<style scoped>
.table {
    margin-top: 20px;
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