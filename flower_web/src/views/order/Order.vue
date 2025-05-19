<template>
    <div class="container">

        <!--表格数据-->
        <div class="table">

            <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%">
                <el-table-column label="序号" width="70" type="index" :index="indexMethod"/>
                <el-table-column prop="cover_url" label="订单图片" width="125">
                    <template #default="scope">
                        <el-image style="width: 100px; height: 50px"
                                  :src="scope.row.flower_img"></el-image>

                    </template>
                </el-table-column>
                <el-table-column prop="username" label="用户" width="150"/>
                <el-table-column prop="quantity" label="购买数量" width="100"/>
                <el-table-column prop="total_price" label="总价格" width="120"/>
                <el-table-column prop="order_status_text" label="订单状态" width="100"/>
                <el-table-column prop="order_num" label="订单号" width="210"/>
                <el-table-column prop="create_time" label="创建时间" width="200"/>

                <el-table-column label="操作" width="140">
                    <template #default="scope">
                        <el-button type="danger" @click="deleteOrder(scope.row)" size="small">删除</el-button>
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
                    <el-form-item label="轮播图链接" prop="link">
                        <el-input v-model="img_url" style="width: 100%" placeholder="输入轮播图链接">
                            <template #prefix>
                                <el-icon class="el-input__icon">
                                    <Link/>
                                </el-icon>
                            </template>
                        </el-input>
                    </el-form-item>

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
import {Link} from "@element-plus/icons-vue";
import usePage from "@/hooks/usePage.js";
import {OrderListRequest, deleteOrderRequest} from "@/apis/order.js";
const tableData = ref([])  // 表格数据
const {
    pageSize,
    currentPage,
    handleSizeChange,
    handleCurrentChange,
    indexMethod
} = usePage()  // 分页


// 发送请求获取订单列表
async function getOrderList() {
    const res = await OrderListRequest()
    tableData.value = res
}

onMounted(() => getOrderList())

// 删除逻辑
async function deleteOrder(row) {
    console.log(row)
    await deleteOrderRequest(row.id)
    getOrderList()
    ElMessage({
        type: "success",
        message: '删除成功'
    })
}


</script>

<style scoped>


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