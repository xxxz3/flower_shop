<template>
    <div class="container">

        <div class="nav">
            <div>
                <el-input v-model="input_flower" style="width: 240px;" placeholder="输入鲜花名称查询">
                    <template #prefix>
                        <el-icon class="el-input__icon">
                            <search/>
                        </el-icon>
                    </template>
                    <template #append>
                        <el-button @click="searchFlower">查 询</el-button>
                    </template>
                </el-input>
            </div>
            <div class="add_btn">
                <el-button type="primary" class="btn" @click="dialogVisible = true" v-if="role == 2">新 增</el-button>
            </div>
        </div>

        <!--表格数据-->
        <div class="table">
            <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border style="width: 100%">
                <el-table-column label="序号" width="70" type="index" :index="indexMethod"
                                 style="background-color: #ffb0b0"/>
                <el-table-column prop="name" label="鲜花名称" width="130"/>
                <el-table-column prop="cover_url" label="图片" width="146">
                    <template #default="scope">
                        <el-image style="width: 120px; height: 100px"
                                  :src="scope.row.image"></el-image>

                    </template>
                </el-table-column>
                <el-table-column prop="price" label="鲜花价格" width="130"/>
                <el-table-column prop="stock" label="剩余数量" width="160"/>
                <el-table-column prop="flower_language" label="花语" width="210" show-overflow-tooltip/>
                <el-table-column prop="create_time" label="创建时间" width="200"/>

                <el-table-column label="操作" width="140">
                    <template #default="scope">
                        <el-button type="danger" @click="deleteFlower(scope.row)" size="small" v-if="role == 2">删除</el-button>
                        <el-button type="primary" @click="PurchaseFlower(scope.row)" size="small">订购</el-button>
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


  <!--  添加鲜花-->
    <el-dialog
            v-model="dialogVisible"
            title="添加鲜花"
            width="500"
            :close-on-click-modal="false"
    >
        <template #footer>
            <div class="dialog-footer">
                <el-form
                        ref="ruleFormRef"
                        style="max-width: 600px"
                        label-width="auto">

                    <el-form-item label="鲜花名称" prop="name">
                        <el-input v-model="name" style="width: 100%" placeholder="输入鲜花名称"></el-input>
                    </el-form-item>

                    <el-form-item label="花语" prop="flower_language">
                        <el-input v-model="flower_language" style="width: 100%" placeholder="花语"></el-input>
                    </el-form-item>

                    <el-form-item label="鲜花总数量" prop="stock">
                        <el-input v-model="stock" style="width: 100%" placeholder="数量"></el-input>
                    </el-form-item>

                    <el-form-item label="鲜花价格" prop="price">
                        <el-input-number v-model="price" :precision="2" :step="0.1"/>
                    </el-form-item>

                    <div class="btn-addFlower">
                        <span style="color: #606266;font-size: 14px; margin-left: 15px;">鲜花图片</span>
                        <input type="file" style="margin-left: 12px" @change="flowerChange">
                        <img :src="previewImg" alt="" id="preview" title="预览图"/>
                    </div>


                </el-form>

                <el-button @click="dialogVisible = false">取消</el-button>
                <el-button type="primary" @click="addFlower">
                    确定
                </el-button>
            </div>
        </template>
    </el-dialog>


  <!--  订购鲜花-->
    <el-dialog
            v-model="FlowerDialogVisible"
            title="鲜花订购"
            width="500"
            :close-on-click-modal="false"
    >
        <template #footer>
            <div class="dialog-footer">
                <el-form
                        ref="ruleFormRef"
                        style="max-width: 600px"
                        label-width="auto">

                    <el-form-item>
                        <div class="flower-title">您正在订购 <span class="text">{{ flower_name }}</span></div>
                    </el-form-item>

                    <el-form-item label="订购数量" prop="price">
                        <el-input-number v-model="num" :min="1" :max="10" @change="handleChange"/>
                    </el-form-item>

                </el-form>

                <el-button @click="FlowerDialogVisible = false">取消</el-button>
                <el-button type="primary" @click="purchaseFlower">
                    确定
                </el-button>
            </div>
        </template>
    </el-dialog>

</template>

<script setup>
import {ref, onMounted} from "vue";
import {ElMessage} from "element-plus";
import {FlowerRequest, DelFlowerRequest, addFlowerRequest} from "@/apis/flower.js";
import {Search} from "@element-plus/icons-vue";
import usePage from "@/hooks/usePage.js";
import {purchaseFlowerRequest} from "@/apis/order.js";
import useRole from "@/hooks/useRole.js";


// 查询输入框
const input_flower = ref('')
const tableData = ref([])  // 表格数据
const {
    pageSize,
    currentPage,
    handleSizeChange,
    handleCurrentChange,
    indexMethod
} = usePage()  // 分页
const dialogVisible = ref(false)  // 弹出框
const FlowerDialogVisible = ref(false)  // 订购鲜花弹出框
const previewImg = ref('')  // 预览图
const name = ref('')  // 鲜花名
const flower_language = ref('')  // 花语
const price = ref('')  // 价格
const stock = ref('')  // 添加鲜花数量
const num = ref(1)  // 订购鲜花数量
const flower_name = ref('')  // 鲜花名字
const flower_id = ref(null)  // 鲜花id
const {role} = useRole()


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

// 新增鲜花
async function addFlower() {
    const res = await addFlowerRequest({
        name: name.value,
        price: price.value,
        flower_language: flower_language.value,
        image: previewImg.value,
        stock: stock.value
    })
    ElMessage.success('添加成功')
    dialogVisible.value = false
    getFlowerList()

}


// 发送请求获取轮播图列表
async function getFlowerList() {
    const res = await FlowerRequest()
    tableData.value = res
    console.log(res)
}

onMounted(() => getFlowerList())

// 删除逻辑
async function deleteFlower(row) {
    await DelFlowerRequest(row.id)
    getFlowerList()
    ElMessage({
        type: "success",
        message: '删除成功'
    })
}


// 查询功能
// 根据鲜花名称进行查询
async function searchFlower() {
    const res = await FlowerRequest(input_flower.value)
    tableData.value = res
}


// 订购鲜花按键
function PurchaseFlower(row) {
    FlowerDialogVisible.value = true
    flower_name.value = row.name
    flower_id.value = row.id
}


// 订购鲜花发送请求
async function purchaseFlower() {
    const res = await purchaseFlowerRequest(
        {
            flower: flower_id.value,
            quantity: num.value
        }
    )
   ElMessage.success('订购成功')
    getFlowerList()
    FlowerDialogVisible.value = false
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

.nav {
    display: flex;
    flex-direction: row;
    margin-bottom: 20px;
}

.add_btn {
    margin-left: 20px;
}

.btn-addFlower {
    display: flex;
    flex-direction: row;
    justify-content: left;
}

#preview {
    height: 120px;
    width: 100px;
    margin-bottom: 20px;
    margin-left: -63px;
}

.flower-title {
    margin-left: 13px;
    font-size: 16px;
}

.text {
    color: #ffb0b0;
    font-size: 18px;
}

</style>