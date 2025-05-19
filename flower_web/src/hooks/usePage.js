import {ref} from "vue";

// 需要将定义的函数暴露给外界
export default function () {
    const pageSize = ref(10)  // 每页多少数据
    const currentPage = ref(1)  // 当前页数

// 当前页面的数据
    const handleSizeChange = (val) => {
        // 将最新的值赋值给pageSize
        pageSize.value = val
    }

// 当前点击的页数
    const handleCurrentChange = (val) => {
        // 将最新的页数赋值给currentPage
        currentPage.value = val
    }


// 表格序号
    const indexMethod = (index) => {
        return index + 1
    }


    // 向外部提供所需要的东西
    return {
        pageSize,
        currentPage,
        handleSizeChange,
        handleCurrentChange,
        indexMethod
    }
}