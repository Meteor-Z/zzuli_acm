<!-- 这里需要改变ip地址，前端需要发送请求，需要改动到这里 -->
<!-- 全局搜索axios请求，然后更改ip地址即可，默认是 localhost:3000 -->
<template>
    <div class="table">
        <el-row justify="center">
            <el-text class="title">郑州轻工业大学程序设计班级天梯赛 - 后台设置</el-text>
        </el-row>
        <div>
            <el-row :gutter="8" style="margin-top: 25px;" justify="center">
                <el-col :span="4" style="margin-top: 5px;"><span>PTA账号数据 (PTA_Session)：</span></el-col>
                <el-col :span="8"><el-input v-model="input_Session" clearable placeholder="请输入PTA_Session" /></el-col>
            </el-row>
            <el-row :gutter="8" style="margin-top: 20px;" justify="center">
                <el-col :span="4" style="margin-top: 5px;"><span>PTA题目集 (Problem_Set)：</span></el-col>
                <el-col :span="8"><el-input v-model="input_SetID" clearable placeholder="请输入Problem_Set" /></el-col>
            </el-row>
            <el-row :gutter="8" style="margin-top: 20px;" justify="center">
                <el-col :span="4" style="margin-top: 5px;"><span>本次比赛显示名称 (Name)：</span></el-col>
                <el-col :span="8"><el-input v-model="input_Title" clearable placeholder="请输入比赛名称" /></el-col>
            </el-row>
            <el-row :gutter="8" style="margin-top: 20px;" justify="center">
                <el-col :span="4" style="margin-top: 5px;"><span>初级阶段最低达标分数：</span></el-col>
                <el-col :span="8"><el-input v-model="input_standard1" clearable placeholder="请输入整数" /></el-col>
            </el-row>
            <el-row :gutter="8" style="margin-top: 20px;" justify="center">
                <el-col :span="4" style="margin-top: 5px;"><span>进阶阶段最低达标分数：</span></el-col>
                <el-col :span="8"><el-input v-model="input_standard2" clearable placeholder="请输入整数" /></el-col>
            </el-row>
            <el-row :gutter="8" style="margin-top: 20px;" justify="center">
                <el-col :span="4" style="margin-top: 5px;"><span>登顶阶段最低达标分数：</span></el-col>
                <el-col :span="8"><el-input v-model="input_standard3" clearable placeholder="请输入整数" /></el-col>
            </el-row>
            <el-row style="margin-top: 40px;" justify="center">
                <el-col :span="3">
                    <el-button @click="SubmitData" icon="Upload">提交数据</el-button>
                </el-col>
                <el-col :span="3" style="margin-left:25px;">
                    <el-button @click="DownData_Single" icon="Download">导出个人榜单</el-button>
                </el-col>
                <el-col :span="3" :push="1">
                    <el-button @click="DownData_Team" icon="Download">导出团队榜单</el-button>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import {ElMessage} from 'element-plus';
import ExcelJS from 'exceljs';
export default {
    setup() {
        const Competition_data = ref([]);
        const input_Session = ref('');
        const input_SetID = ref('');
        const input_Title = ref('');
        const input_standard1 = ref('');
        const input_standard2 = ref('');
        const input_standard3 = ref('');
        const fetchData = async () => {
            try {
                const response = await axios.get(`http://localhost:3000/competition/data`);
                Competition_data.value = response.data[0];
                input_Session.value = Competition_data.value.PTA_session;
                input_SetID.value = Competition_data.value.Problem_Set;
                input_Title.value = Competition_data.value.Title;
                input_standard1.value = Competition_data.value.standard1;
                input_standard2.value = Competition_data.value.standard2;
                input_standard3.value = Competition_data.value.standard3;
            } catch (error) {
                console.error('Error fetching competition data:', error);
            }
        };

        const SubmitData = async () => {
            axios.post(`http://localhost:3000/competition/set_title/${input_Title.value}`)
                .then(response => {
                    if (response.data.message == "success") {
                        ElMessage({ showClose: true, message: '提交比赛标题成功！', duration: 5000, type: 'success' });
                    } else {
                        ElMessage({ showClose: true, message: '提交比赛标题失败！', duration: 5000, type: 'error' });
                    }
                })
                .catch(error => {
                    ElMessage({ showClose: true, message: '提交比赛标题失败！', duration: 5000, type: 'error' });
                });
            axios.post(`http://localhost:3000/competition/set_pta/${input_Session.value}/${input_SetID.value}`)
                .then(response => {
                    if (response.data.message == "success") {
                        ElMessage({ showClose: true, message: '提交PTA数据成功！', duration: 4000, type: 'success' });
                    } else {
                        ElMessage({ showClose: true, message: '提交PTA数据失败！', duration: 4000, type: 'error' });
                    }
                })
                .catch(error => {
                    ElMessage({ showClose: true, message: '提交PTA数据失败！', duration: 4000, type: 'error' });
                });
            axios.post(`http://localhost:3000/competition/set_standard/${input_standard1.value}/${input_standard2.value}/${input_standard3.value}`)
              .then(response => {
                    if(response.data.message == "success"){
                        ElMessage({ showClose: true, message: '提交成绩标准成功！', duration: 3000, type: 'success' });
                    } else{
                        ElMessage({ showClose: true, message: '提交成绩标准失败！', duration: 3000, type: 'error' });
                    }
                })
                .catch(error => {
                    ElMessage({ showClose: true, message: '提交成绩标准失败！', duration: 3000, type: 'error' });
                });
        };

        const DownData_Single = async () => {
            axios.get(`http://localhost:3000/students`)
                .then(response => {
                    const data=response.data;
                    exportToExce_single(data);
                })
                .catch(error => {
                    ElMessage({ showClose: true, message: '获取排名信息失败！', duration: 5000, type: 'error' });
                });
        };

        const exportToExce_single = async (data) => {
            const workbook = new ExcelJS.Workbook();
            const sheet = workbook.addWorksheet('Single Rank');
            /*-------------------------------------------添加表格标题行-------------------------------------------*/
            const titleRow = sheet.addRow(['郑州轻工业大学2023级程序设计天梯赛 - 个人排名']); // 添加标题行
            titleRow.height = 34; // 设置标题行高
            sheet.mergeCells('A1:W1'); // 合并单元格
            const titleCell = titleRow.getCell(1);
            titleCell.font = { size: 16, name: 'Microsoft YaHei', bold: true }; // 设置标题字体
            titleCell.alignment = { horizontal: 'center', vertical: 'middle' }; // 设置标题居中对齐
            titleCell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: '808080' } }; // 设置标题背景颜色
            titleCell.border = {
                top: { style: 'thin', color: { argb: '000000' } },
                left: { style: 'thin', color: { argb: '000000' } },
                bottom: { style: 'thin', color: { argb: '000000' } },
                right: { style: 'thin', color: { argb: '000000' } },
            };
            /*-------------------------------------------添加表格表头行-------------------------------------------*/
            const headerRow = sheet.addRow(['排名','姓名', '学号', '班级', '1-1', '1-2', '1-3', '1-4', '1-5', '1-6', '1-7', '1-8', 
            '2-1', '2-2', '2-3', '2-4', '3-1', '3-2', '3-3', '基础分', '进阶分', '登顶分', '总分']);
            for (let col = 1; col <= 23; col++) {
                const cell = sheet.getCell(2, col);
                cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'A6A6A6' } };
            }
            headerRow.alignment = { horizontal: 'center', vertical: 'middle' };
            headerRow.font = { bold: true, name: 'Microsoft YaHei' };
            headerRow.eachCell((cell) => {
                cell.border = {
                    top: { style: 'thin', color: { argb: '000000' } },
                    left: { style: 'thin', color: { argb: '000000' } },
                    bottom: { style: 'thin', color: { argb: '000000' } },
                    right: { style: 'thin', color: { argb: '000000' } },
                };
            });
            /*-------------------------------------------添加表格数据行-------------------------------------------*/
            data.forEach(item => {
                const row = sheet.addRow([item.rank, item.name, item.stu_id, item.class, item.p11, item.p12, item.p13, item.p14
                , item.p15, item.p16, item.p17, item.p18, item.p21, item.p22, item.p23, item.p24, item.p31, item.p32, item.p33
                , item.part1, item.part2, item.part3, item.score]);
                row.eachCell((cell) => {
                    cell.alignment = { horizontal: 'center', vertical: 'middle' };
                    cell.border = {
                        top: { style: 'thin', color: { argb: '000000' } },
                        left: { style: 'thin', color: { argb: '000000' } },
                        bottom: { style: 'thin', color: { argb: '000000' } },
                        right: { style: 'thin', color: { argb: '000000' } },
                    };
                });
            });
            /*-------------------------------------------设置表格单元格-------------------------------------------*/
            sheet.getColumn(2).width = 9;
            sheet.getColumn(3).width = 15;
            sheet.getColumn(4).width = 30;
            for (let col = 5; col <= 19; col++) {
                sheet.getColumn(col).width = 6;
            }

            // 创建一个Blob对象
            const blob = await workbook.xlsx.writeBuffer();
            // 创建一个Blob URL，并创建一个a标签用于下载
            const blobUrl = URL.createObjectURL(new Blob([blob], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' }));
            const link = document.createElement('a');
            link.href = blobUrl;
            link.download = '郑州轻工业大学2023级程序设计天梯赛_个人榜.xlsx'; //导出的文件名
            document.body.appendChild(link);
            link.click();
            // 移除a标签和Blob URL
            document.body.removeChild(link);
            URL.revokeObjectURL(blobUrl);
        };

        const DownData_Team = async () => {
            axios.get(`http://localhost:3000/teams`)
                .then(response => {
                    const data = response.data;
                    exportToExce_Team(data);
                })
                .catch(error => {
                    ElMessage({ showClose: true, message: '获取排名信息失败！', duration: 5000, type: 'error' });
                });
        };

        const exportToExce_Team = async (data) => {
            const workbook = new ExcelJS.Workbook();
            const sheet = workbook.addWorksheet('Single Rank');
            /*-------------------------------------------添加表格标题行-------------------------------------------*/
            const titleRow = sheet.addRow(['郑州轻工业大学2023级程序设计天梯赛 - 团队排名']); // 添加标题行
            titleRow.height = 34; // 设置标题行高
            sheet.mergeCells('A1:G1'); // 合并单元格
            const titleCell = titleRow.getCell(1);
            titleCell.font = { size: 16, name: 'Microsoft YaHei', bold: true }; // 设置标题字体
            titleCell.alignment = { horizontal: 'center', vertical: 'middle' }; // 设置标题居中对齐
            titleCell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: '808080' } }; // 设置标题背景颜色
            titleCell.border = {
                top: { style: 'thin', color: { argb: '000000' } },
                left: { style: 'thin', color: { argb: '000000' } },
                bottom: { style: 'thin', color: { argb: '000000' } },
                right: { style: 'thin', color: { argb: '000000' } },
            };
            /*-------------------------------------------添加表格表头行-------------------------------------------*/
            const headerRow = sheet.addRow(['排名', '队伍名称', '班级', '基础分', '进阶分', '登顶分', '总分']);
            for (let col = 1; col <= 7; col++) {
                const cell = sheet.getCell(2, col);
                cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'A6A6A6' } };
            }
            headerRow.alignment = { horizontal: 'center', vertical: 'middle' };
            headerRow.font = { bold: true, name: 'Microsoft YaHei' };
            headerRow.eachCell((cell) => {
                cell.border = {
                    top: { style: 'thin', color: { argb: '000000' } },
                    left: { style: 'thin', color: { argb: '000000' } },
                    bottom: { style: 'thin', color: { argb: '000000' } },
                    right: { style: 'thin', color: { argb: '000000' } },
                };
            });
            /*-------------------------------------------添加表格数据行-------------------------------------------*/
            data.forEach(item => {
                const row = sheet.addRow([item.rank, item.TeamName, item.Class, item.part1, item.part2, item.part3, item.score]);
                row.eachCell((cell) => {
                    cell.alignment = { horizontal: 'center', vertical: 'middle' };
                    cell.border = {
                        top: { style: 'thin', color: { argb: '000000' } },
                        left: { style: 'thin', color: { argb: '000000' } },
                        bottom: { style: 'thin', color: { argb: '000000' } },
                        right: { style: 'thin', color: { argb: '000000' } },
                    };
                });
            });
            /*-------------------------------------------设置表格单元格-------------------------------------------*/
            sheet.getColumn(2).width = 40;
            sheet.getColumn(3).width = 30;
            // 创建一个Blob对象
            const blob = await workbook.xlsx.writeBuffer();
            // 创建一个Blob URL，并创建一个a标签用于下载
            const blobUrl = URL.createObjectURL(new Blob([blob], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' }));
            const link = document.createElement('a');
            link.href = blobUrl;
            link.download = '郑州轻工业大学2023级程序设计天梯赛_团队榜.xlsx'; //导出的文件名
            document.body.appendChild(link);
            link.click();
            // 移除a标签和Blob URL
            document.body.removeChild(link);
            URL.revokeObjectURL(blobUrl);
        };

        onMounted(() => {
            fetchData();
        });
        return {
            Competition_data,
            fetchData,
            input_Session,
            input_SetID,
            input_Title,
            input_standard1,
            input_standard2,
            input_standard3,
            SubmitData,
            exportToExce_single,
            exportToExce_Team,
            DownData_Single,
            DownData_Team,
        };
    },
};
</script>

<style scoped>
::v-deep .el-input__wrapper{
    backdrop-filter: blur(10px);
    --el-input-text-color: rgb(255, 255, 255);
    --el-input-bg-color: rgba(55, 55, 55, 0.189);
    --el-input-clear-hover-color:rgba(222, 222, 222, 0.925);
    --el-input-focus-border:rgb(218, 218, 218)!important;
    --el-input-focus-border-color:rgb(211, 211, 211)!important;
}

::v-deep .el-button{
    --el-button-text-color:aliceblue;
    background-color: rgb(149, 0, 255);
    --el-button-hover-text-color: rgb(255, 255, 255);
    --el-button-hover-border-color:rgb(255, 255, 255);
    --el-button-active-text-color:rgba(255, 255, 255, 0.886);
    --el-button-active-border-color:rgba(255, 255, 255, 0.865);
}

.table {
  display: flex;
  flex-direction: column;
  width: 80%;
  margin: 2px auto;
  padding: 30px;
  position: relative;
  overflow: hidden;
}

.table::before{
  content: '';
  position: absolute;
  top: 0;bottom: 0;left: 0;right: 0;
  background: rgba(155, 155, 155, 0.146);
  background: url("../assets/Images/313353.jpg")  0 / cover fixed;
  filter: blur(20px);
  margin: -30px;
}

.title{
    font-weight: bold;
    font-size: 25px;
    color:aliceblue;
}
</style>