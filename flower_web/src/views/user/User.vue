<template>
    <div class="container">

        <!-- 搜索-->
        <div class="input_search">
            <el-input v-model="input_name" style="width: 280px; margin-left: 20px" placeholder="输入姓名或用户名查询">
                <template #prefix>
                    <el-icon class="el-input__icon">
                        <search/>
                    </el-icon>
                </template>
                <template #append>
                    <el-button @click="searchName">查 询</el-button>
                </template>
            </el-input>

        </div>

        <!--表格数据-->
        <div class="table">
            <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%">
                <el-table-column label="序号" width="80" type="index" :index="indexMethod"/>
                <el-table-column prop="username" label="用户名" width="100"/>
                <el-table-column prop="name" label="姓名" width="100"/>
                <el-table-column prop="role_text" label="角色" width="100"/>
                <el-table-column prop="sex_text" label="性别" width="60"/>
                <el-table-column prop="phone" label="电话" width="120"/>
                <el-table-column prop="addr" label="地址" width="120"/>
                <el-table-column prop="create_time" label="创建时间" width="180"/>

                <el-table-column label="操作">
                    <template #default="scope">
                        <el-button type="danger" @click="deleteUser(scope.row)" size="small">删除</el-button>
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


</template>

<script setup>
import {ref, onMounted} from "vue";
import {Search} from '@element-plus/icons-vue'
import {getUserRequest, deleteUserRequest, getUserNameRequest} from "@/apis/user.js";
import {ElMessage} from "element-plus";
import usePage from "@/hooks/usePage.js";


// 查询输入框
const input_name = ref('')

// 表格数据
const tableData = ref([])

const {
    pageSize,
    currentPage,
    handleSizeChange,
    handleCurrentChange,
    indexMethod
} = usePage()  // 分页

// 发送请求获取用户列表
async function getUserList() {
    const res = await getUserRequest()
    tableData.value = res
}

onMounted(() => getUserList())


// 删除逻辑
async function deleteUser(row) {
    await deleteUserRequest(row.id)
    ElMessage({
        type: "success",
        message: '删除成功'
    })
    getUserList()
}


// 查询功能
// 根据姓名进行查询
async function searchName() {
    const res = await getUserNameRequest(input_name.value)
    tableData.value = res
}

</script>

<style scoped>
.table {
    margin-top: 20px;
}


.input_search {
    margin-left: -19px;
}
</style>