<!-- 这里需要改变ip地址，前端需要发送请求，需要改动到这里 -->
<!-- 全局搜索axios请求，然后更改ip地址即可，默认是 localhost:3000 -->
<template>
    <br>
    <el-row justify="center">
        <el-col :span="5" :push="3" style="margin-bottom: 10px;">
            <el-input v-model="searchName" placeholder="输入队伍名称" />
        </el-col>
        <el-col :span="2" :push="3">
            <el-button @click="handleSearch" icon="Search">搜索</el-button>
        </el-col>
        <el-col :span="6" :push="3" style="margin-top: 2px;">
            <el-text>
              <el-icon><InfoFilled /></el-icon>
                榜单数据每15秒刷新一次，请在15秒后刷新页面获取最新数据。
            </el-text>
        </el-col>
    </el-row>
    <hr style="background-color:rgb(71, 71, 71); border: none; height: 1px;">
    <div class="table">
        <el-row class="single" v-for="teams_col in filteredTeams" :key="teams_col.prop" @click="handleRowClick(teams_col)">
            <div class="badge">
                <span><i>{{ teams_col.rank }}</i></span>
            </div>
            <div class="progress">
                <div class="head">
                  <img src="../assets/Images/zzuli.png">
                </div>
                <div class="progress1">
                  <span style="color:white;display: inline-block;white-space: nowrap">
                        {{ teams_col.TeamName ? `${teams_col.TeamName}` : '---' }}——{{ teams_col.Class ? `${teams_col.Class}` : '---' }}&nbsp;
                    <el-tooltip class="item" effect="dark" content="第一阶段等级" placement="top">
                      <svg v-if="teams_col.part1 > 0" class="icon" aria-hidden="true" color="#6FE0FF">
                        <use v-if="teams_col.part1 === teams_col.sum1" xlink:href="#icon-dengji-A"></use>
                        <use v-else-if="teams_col.part1 >= standard1" xlink:href="#icon-dengji-B"></use>
                        <use v-else-if="teams_col.part1 < standard1" xlink:href="#icon-dengji-C"></use>
                      </svg>
                    </el-tooltip>
                    <el-tooltip class="item" effect="dark" content="第二阶段等级" placement="top">
                      <svg v-if="teams_col.part2 > 0" class="icon" aria-hidden="true" color="#DCB672">
                        <use v-if="teams_col.part2 === teams_col.sum2" xlink:href="#icon-dengji-A"></use>
                        <use v-else-if="teams_col.part2 >= standard2" xlink:href="#icon-dengji-B"></use>
                        <use v-else-if="teams_col.part2 < standard2" xlink:href="#icon-dengji-C"></use>
                      </svg>
                    </el-tooltip>
                    <el-tooltip class="item" effect="dark" content="第三阶段等级" placement="top">
                      <svg v-if="teams_col.part3 > 0" class="icon" aria-hidden="true" color="#DC7272">
                        <use v-if="teams_col.part3 === teams_col.sum3" xlink:href="#icon-dengji-A"></use>
                        <use v-else-if="teams_col.part3 >= teams_col.sum3 / 2" xlink:href="#icon-dengji-B"></use>
                        <use v-else-if="teams_col.part3 < teams_col.sum3 / 2" xlink:href="#icon-dengji-C"></use>
                      </svg>
                    </el-tooltip>
                  </span>
                  <el-tooltip class="item" effect="dark" :content="teams_col.part1 + '/' + teams_col.sum1" placement="bottom">
                        <img src="../assets/Images/progress_blue.png" :style="{ width: (teams_col.part1 / teams_col.sum1) * 100 + '%' , height: '20px'}">
                  </el-tooltip>
                  <img v-show="teams_col.part1 >= 0 && (teams_col.part1 < standard1 || teams_col.part2 === 0)"
                           src="../assets/Images/circle_blue.png" class="circleStyle"
                           :style="{ left: (teams_col.part1 / teams_col.sum1) * 100 + '%' }">
                </div>
                <div class="point_sm"></div>
                <div class="progress1">
                    <el-tooltip class="item" effect="dark" :content="teams_col.part2 + '/' + teams_col.sum2" placement="bottom">
                        <img v-if="teams_col.part1 >= standard1" src="../assets/Images/progress_orange.png"
                             :style="{ width: (teams_col.part2 / teams_col.sum2) * 100 + '%' , height:'20px'}">

                        <img v-else src="../assets/Images/progress_gray.png"
                             :style="{ width: (teams_col.part2 / teams_col.sum2) * 100 + '%', height: '20px' }">
                    </el-tooltip>
                    <img
                        v-show="(teams_col.part2 > 0 || teams_col.part1 === teams_col.sum1) && teams_col.part1 >= standard1 && (teams_col.part3 === 0 || teams_col.part2 < standard2)"
                        src="../assets/Images/circle_yellow.png" class="circleStyle"
                        :style="{ left: (teams_col.part2 / teams_col.sum2) * 100 + '%' }">
                </div>
                <div class="point_sm"></div>
                <div class="progress2">
                    <el-tooltip class="item" effect="dark" :content="teams_col.part3 + '/' + teams_col.sum3" placement="bottom">
                    <img v-if="teams_col.part2 >= standard2 && teams_col.part1 >= standard1"
                         src="../assets/Images/progress_red.png" :style="{ width: (teams_col.part3 / teams_col.sum3) * 100 + '%', height:'20px' }">
                    <img v-else src="../assets/Images/progress_gray.png"
                         :style="{ width: (teams_col.part3 / teams_col.sum3) * 100 + '%', height: '20px' }">
                    </el-tooltip>
                    <img v-show="teams_col.part1 >= standard1 && teams_col.part2 >= standard2 && teams_col.part3 > 0"
                         src="../assets/Images/circle_red.png" class="circleStyle"
                         :style="{ left: (teams_col.part3 / teams_col.sum3) * 100 + '%' }">
                </div>
                <div class="point_big"></div>
            </div>
            <div class="score">
                <span><i>{{ teams_col.score }}</i></span>
            </div>
        </el-row>
    </div>
    <div>
        <el-dialog v-model="dialogVisible" :title="dialogTitle" @close="dialogVisible = false" :width="'80%'" center>
            <el-table v-if="isMobile" :header-cell-class-name="addClass" stripe :cell-class-name="addCell" :data="students"
            :cell-style="{ textAlign: 'center' }" :header-cell-style="{ 'text-align': 'center' }" style="width: 100%">
                <el-table-column v-for="column in students_columns" :key="column.prop" :prop="column.prop" :label="column.label" :width="column.width">
                </el-table-column>
            </el-table>
            <el-table v-else :header-cell-class-name="addClass" stripe :cell-class-name="addCell" :data="students" class="info-set"
                :cell-style="{ textAlign: 'center' }" :header-cell-style="{ 'text-align': 'center' }" style="width: 100%">
                    <el-table-column v-for="column in students_columns" :key="column.prop" :prop="column.prop" :label="column.label" :width="column.width">
                    </el-table-column>
            </el-table>
        </el-dialog>
    </div>
</template>

<script>
import '../assets/iconfont'
import { ref, onMounted, watchEffect } from 'vue';
import axios from 'axios';

export default {
    setup(){
        const teams = ref([]);
        const searchName = ref('');
        const filteredTeams = ref([]);
        const standard1 = ref(0);
        const standard2 = ref(0);
        const standard3 = ref(0);
        const dialogVisible = ref(false);
        const dialogTitle = ref('');
        const students = ref([]);
        const isMobile = ref(true);
        const students_columns = [
            { prop: 'rank', label: '排名', width: "55" },
            { prop: 'name', label: '姓名', width: "80" },
            { prop: 'p11', label: '1-1', width: "55" },
            { prop: 'p12', label: '1-2', width: "55" },
            { prop: 'p13', label: '1-3', width: "55" },
            { prop: 'p14', label: '1-4', width: "55" },
            { prop: 'p15', label: '1-5', width: "55" },
            { prop: 'p16', label: '1-6', width: "55" },
            { prop: 'p17', label: '1-7', width: "55" },
            { prop: 'p18', label: '1-8', width: "55" },
            { prop: 'p21', label: '2-1', width: "55" },
            { prop: 'p22', label: '2-2', width: "55" },
            { prop: 'p23', label: '2-3', width: "55" },
            { prop: 'p24', label: '2-4', width: "55" },
            { prop: 'p31', label: '3-1', width: "55" },
            { prop: 'p32', label: '3-2', width: "55" },
            { prop: 'p33', label: '3-3', width: "55" },
            { prop: 'part1', label: '基础分', width: "70" },
            { prop: 'part2', label: '进阶分', width: "70" },
            { prop: 'part3', label: '登顶分', width: "70" },
            { prop: 'score', label: '总分', width: "65" },
        ];

        const fetchData = async () => {
            try {
                const res_standard = await axios.get(`http://localhost:3000/competition/standard`);
                standard1.value = res_standard.data[0].standard1;
                standard2.value = res_standard.data[0].standard2;
                standard3.value = res_standard.data[0].standard3;
                const response = await axios.get(`http://localhost:3000/teams`);
                teams.value = response.data;
                handleSearch();
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        const handleSearch = () => {
            if (searchName.value.trim() === '') {
                filteredTeams.value = teams.value;
            } else {
                filteredTeams.value = teams.value.filter(
                    (team) => team.TeamName.includes(searchName.value)
                );
            }
        };

        const calculatePercentage = (part, total) => {
            return (part / total) * 100;
        };

        const formatProgress = (part, total) => {
            return `${part}/${total}`;
        };

        const handleRowClick = async(row) => {
            try{
                const response = await axios.get(`http://localhost:3000/students/students_by_id/${row.TeamID}`);
                students.value = response.data;
            } catch(error){
                console.error('Error fetching msg_students data:', error);
            }
            dialogTitle.value = `${row.Class} —— ${row.TeamName}`;
            dialogVisible.value = true;
        };

        const addClass = ({ row, column, rowIndex, columnIndex }) => {
            if (columnIndex >= 2 && columnIndex <= 9) {
                return 'part1-row';
            }
            else if (columnIndex >= 10 && columnIndex <= 13) {
                return 'part2-row';
            }
            else if (columnIndex >= 14 && columnIndex <= 16) {
                return 'part3-row';
            }
        };

        const addCell = ({ row, column, rowIndex, columnIndex }) => {
            if (columnIndex >= 2 && columnIndex <= 9) {
                return 'part1-row-back';
            }
            else if (columnIndex >= 10 && columnIndex <= 13) {
                return 'part2-row-back';
            }
            else if (columnIndex >= 14 && columnIndex <= 16) {
                return 'part3-row-back';
            }
        };

        watchEffect(() => {
            isMobile.value = window.innerWidth <= 1200;
        });
        
        onMounted(() => {
          fetchData();
        });
        return {
            teams,
            searchName,
            filteredTeams,
            handleSearch,
            calculatePercentage,
            formatProgress,
            standard1,
            standard2,
            standard3,
            students,
            students_columns,
            handleRowClick,
            addCell,
            addClass,
            isMobile,
            dialogTitle,
            dialogVisible,
        };
    },
};
</script>

<style scoped>
.search-bar {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 10px;
}

.search-input {
    margin-right: 35px;
}

.search-button {
    flex-shrink: 0;
}

.table-set {
    display: flex;
    justify-content: center;
    align-items: center;
}

.info-set {
    display: flex;
    justify-content: center;
    align-items: center;
}

.custom-progress-text {
  color: #dbdbdb;
  font-size: 12px;
  font-weight: bold;
}

::v-deep .el-table__body tr {
  --el-table-border-color:transparent;
  --el-table-border:0px transparent;
  backdrop-filter: blur(15px);
  background-color: rgba(68, 68, 68, 0.059);
  --el-table-row-hover-bg-color:transparent;
}

::v-deep .el-table__header-wrapper {
  --el-table-border-color:transparent;
  --el-table-border:0px transparent;
  backdrop-filter: blur(10px);
  --el-table-header-bg-color:rgba(86, 0, 103, 0.363) !important;
  --el-table-tr-bg-color:rgba(86, 0, 103, 0.363) !important;
}

::v-deep .el-table__body tr.el-table__row--striped td.el-table__cell{
    background-color: rgba(255, 255, 255, 0.089);
}

::v-deep .el-input__wrapper{
    backdrop-filter: blur(10px);
    --el-input-bg-color: rgba(17, 17, 17, 0.089);
    --el-input-focus-border:blueviolet!important;
    --el-input-focus-border-color:blueviolet!important;
}

::v-deep .el-button{
    --el-button-hover-text-color: blueviolet;
    --el-button-hover-border-color:rgb(100, 34, 163);
    --el-button-active-text-color:blueviolet;
    --el-button-active-border-color:blueviolet;
}

::v-deep .el-dialog{
    backdrop-filter: blur(10px);
    --el-dialog-bg-color:rgba(17, 17, 17, 0.089);
}

::v-deep .el-dialog__header{
    --el-dialog-title-font-size: 24px;
    font-weight: bold;
}

::v-deep .el-progress-bar__outer{
    backdrop-filter: blur(5px);
    background-color: rgba(205, 205, 205, 0.11);
}

::v-deep .el-overlay-dialog{
    backdrop-filter: blur(20px);
}

.el-table >>> .rank-row{
    font-size: 20px;
}

.el-table >>> .team-row{
    font-weight: bold;
    font-size: large;
}

.el-table >>> .part1-row {
  color: rgb(0, 136, 255) !important;
}

.el-table >>> .part2-row {
  color: rgb(255, 196, 0) !important;
}

.el-table >>> .part3-row {
  color: red !important;
}

.el-table >>> .part1-row-back {
  background-color: #02abff4c;
  color:rgb(219, 219, 219);
  font-weight: bold;
}

.el-table >>> .part2-row-back {
  background-color: #cd960c42;
  color:rgb(219, 219, 219);
  font-weight: bold;
}

.el-table >>> .part3-row-back {
  background-color: #cd0c0c42;
  color:rgb(219, 219, 219);
  font-weight: bold;
}

.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.shelter {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.4;
  background: rgb(0, 0, 0);
  z-index: 50;
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
  background: rgba(255,0,0,.5);
  background: url("../assets/Images/313353.jpg")  0 / cover fixed;
  filter: blur(20px);
  margin: -30px;
}

.title {
  font-size: 35px;
  font-weight: bold;
  color: #409EFF;
}

.pagination {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  height: 60px;
}

.single {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  height: 120px;
  padding: 10px 5px;
}

.single:nth-child(even){
  background: rgba(38,50,111,.4);
}

.badge {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 10%;

}
.badge>span{
  color: #FFD700;
  font-size: 40px;
  font-weight: bold;
}
.progress {
  width: 80%;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.score {
  width: 10%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.score > span {
  color: #FFD700;
  font-size: 40px;
  font-weight: bold;
}
.progress1 {
  display: flex;
  flex-direction: row;
  align-items: center;
  background-image: url("../assets/Images/bg1.png");
  width: 32%;
  height: 20px;
  position: relative;
}
.circleStyle{
  display: flex;
  z-index: 1;
  position: absolute;
  margin-left: -5px;
}

.progress2{
  display: flex;
  flex-direction: row;
  align-items: center;
  background-image: url("../assets/Images/bg1.png");
  width: 25%;
  height: 20px;
  position: relative;
}

.progress1 > span {
  position: absolute;
  top: -35px;
  left: 8px;
}

.point_sm {
  display: flex;
  width: 45px;
  height: 50px;
  background-image: url("../assets/Images/6.png");
  background-repeat: no-repeat;
  /*background-size: 30px 42px;*/
}

.point_big {
  display: flex;
  width: 45px;
  height: 50px;
  background-image: url("../assets/Images/6.png");
  background-repeat: no-repeat;

}

.detail {
  position: fixed;
  top: 120px;
  left: calc(50% - 500px);
  z-index: 51;
}

.box-card {
  background: rgba(60, 76, 153, .9);
  width: 1000px;
  /*height: 300px;*/
}

.title_detail {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin:0px auto;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.title_detail > span:nth-child(1) {
  color: #FFD700;
  font-size: 50px;
}

.title_detail > span:nth-child(2) {
  color: white;
  font-size: 40px;
}

.head {
  height: 50px;
  width: 45px;
  border-radius: 50%;
  background-image: url("../assets/Images/point_big.png");
  display: flex;
  justify-content: center;
  align-items: center;
}

table {
  width: 100%;
  text-align: center;
}

td {
  height: 50px;
}

.head > img {
  margin: 0;
  height: 40px;
  width: 40px;
}

.xiahuaxian1{
  text-decoration: line-through;
  text-decoration-color:#FFD700;
}
.xiahuaxian2{
  text-decoration: line-through;
  text-decoration-color:#F04F4F;
}
</style>