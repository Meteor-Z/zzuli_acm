<template>
  <div class="textcon">
    <div style="width:92%; display:block">
      <el-table id="data_acm" :data="students" stripe :cell-style="{ textAlign: 'center' }"
        :header-cell-style="{ 'text-align': 'center' }" style="width: 100%" :header-cell-class-name="addClass"
        :cell-class-name="addCell" border>
        <el-table-column v-for="column in students_columns" :key="column.prop" :prop="column.prop" :label="column.label"
          :width="column.width">
          <template v-if="column.width == 70" #default="scope">
            <p v-if="column.prop ==='strp11'">{{ scope.row.strp11 }}<br>{{ scope.row.tmep11 }}</p>
            <p v-else-if="column.prop ==='strp12'">{{ scope.row.strp12 }}<br>{{ scope.row.tmep12 }}</p>
            <p v-else-if="column.prop ==='strp13'">{{ scope.row.strp13 }}<br>{{ scope.row.tmep13 }}</p>
            <p v-else-if="column.prop ==='strp14'">{{ scope.row.strp14 }}<br>{{ scope.row.tmep14 }}</p>
            <p v-else-if="column.prop ==='strp15'">{{ scope.row.strp15 }}<br>{{ scope.row.tmep15 }}</p>
            <p v-else-if="column.prop ==='strp16'">{{ scope.row.strp16 }}<br>{{ scope.row.tmep16 }}</p>
            <p v-else-if="column.prop ==='strp17'">{{ scope.row.strp17 }}<br>{{ scope.row.tmep17 }}</p>
            <p v-else-if="column.prop ==='strp18'">{{ scope.row.strp18 }}<br>{{ scope.row.tmep18 }}</p>
            <p v-else-if="column.prop ==='strp21'">{{ scope.row.strp21 }}<br>{{ scope.row.tmep21 }}</p>
            <p v-else-if="column.prop ==='strp22'">{{ scope.row.strp22 }}<br>{{ scope.row.tmep22 }}</p>
            <p v-else-if="column.prop ==='strp23'">{{ scope.row.strp23 }}<br>{{ scope.row.tmep23 }}</p>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watchEffect } from 'vue';
import axios from 'axios';
import getConfig from '../../config';
export default {
  setup() {
    const searchName = ref('');
    const filteredStudents = ref([]);
    const students = ref([]);
    const isMobile = ref(false);
    const students_columns = [
      { prop: 'rank', label: '#', width: "60" },
      { prop: 'school', label: 'School', width: "240" },
      { prop: 'subject', label: 'College', width: "240" },
      { prop: 'name', label: 'Name', width: "230" },
      { prop: 'sloved', label: 'Solved', width: "90" },
      { prop: 'penalty', label: 'Penalty', width: "90" },
      { prop: 'strp11', label: 'A', width: "70" },
      { prop: 'strp12', label: 'B', width: "70" },
      { prop: 'strp13', label: 'C', width: "70" },
      { prop: 'strp14', label: 'D', width: "70" },
      { prop: 'strp15', label: 'E', width: "70" },
      { prop: 'strp16', label: 'F', width: "70" },
      { prop: 'strp17', label: 'G', width: "70" },
      { prop: 'strp18', label: 'H', width: "70" },
      { prop: 'strp21', label: 'I', width: "70" },
      { prop: 'strp22', label: 'J', width: "70" },
      { prop: 'strp23', label: 'K', width: "70" },
    ];

    const fetchData = async () => {
      try {
        const apiconfig = getConfig();
        const response = await axios.get(`${apiconfig.apiUrl}/students`);
        students.value = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    const addClass = ({ row, column, rowIndex, columnIndex }) => {
      if (columnIndex < 6) { return 'part0-row'; }
      if (columnIndex == 6) { return 'part1-row'; }
      if (columnIndex == 7) { return 'part2-row'; }
      if (columnIndex == 8) { return 'part3-row'; }
      if (columnIndex == 9) { return 'part4-row'; }
      if (columnIndex == 10) { return 'part5-row'; }
      if (columnIndex == 11) { return 'part6-row'; }
      if (columnIndex == 12) { return 'part7-row'; }
      if (columnIndex == 13) { return 'part8-row'; }
      if (columnIndex == 14) { return 'part9-row'; }
      if (columnIndex == 15) { return 'part10-row'; }
      if (columnIndex == 16) { return 'part11-row'; }
    };

    const addCell = ({ row, column, rowIndex, columnIndex }) => {
      if (columnIndex == 6) {
        if (row.strp11 === "+") {
          return 'green-row';
        }
        else if (row.p11 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp11 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 7) {
        if (row.strp12 === "+") {
          return 'green-row';
        }
        else if (row.p12 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp12 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 8) {
        if (row.strp13 === "+") {
          return 'green-row';
        }
        else if (row.p13 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp13 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 9) {
        if (row.strp14 === "+") {
          return 'green-row';
        }
        else if (row.p14 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp14 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 10) {
        if (row.strp15 === "+") {
          return 'green-row';
        }
        else if (row.p15 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp15 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 11) {
        if (row.strp16 === "+") {
          return 'green-row';
        }
        else if (row.p16 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp16 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 12) {
        if (row.strp17 === "+") {
          return 'green-row';
        }
        else if (row.p17 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp17 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 13) {
        if (row.strp18 === "+") {
          return 'green-row';
        }
        else if (row.p18 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp18 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 14) {
        if (row.strp21 === "+") {
          return 'green-row';
        }
        else if (row.p21 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp21 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 15) {
        if (row.strp22 === "+") {
          row.strp22 = "+"
          return 'green-row';
        }
        else if (row.p22 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp22 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
      if (columnIndex == 16) {
        if (row.strp23 === "+") {
          row.strp23 = "+"
          return 'green-row';
        }
        else if (row.p23 != 0) {
          return 'greensmall-row';
        }
        else if (row.strp23 != "--") {
          return 'redsmall-row';
        }
        else{
          return 'normal-row';
        }
      }
    };

    watchEffect(() => {
      isMobile.value = window.innerWidth <= 1200;
    });

    onMounted(() => {
      fetchData();
    });

    return {
      filteredStudents,
      students_columns,
      students,
      searchName,
      isMobile,
      addClass,
      addCell,
    };
  },
};
</script>

<style scoped>
::v-deep .el-table .cell {
  white-space: pre;
}

::v-deep .el-table__header {
  font-family: CommitMono;
}

::v-deep .el-table__body {
  font-family: Harmony_Bold;
}

.el-table>>>.part0-row {
  color: black;
  background: rgb(252, 237, 153) !important;
}

.el-table>>>.part1-row {
  color: black;
  background: rgb(255, 115, 0) !important;
}

.el-table>>>.part2-row {
  color: black;
  background: rgb(218, 144, 174) !important;
}

.el-table>>>.part3-row {
  color: black;
  background: rgb(214, 54, 121) !important;
}

.el-table>>>.part4-row {
  color: white;
  background: rgb(76, 0, 252) !important;
}

.el-table>>>.part5-row {
  color: black;
  background: rgba(219, 73, 255, 0.651) !important;
}

.el-table>>>.part6-row {
  color: black;
  background: rgb(0, 255, 106) !important;
}

.el-table>>>.part7-row {
  color: white;
  background: rgb(255, 0, 0) !important;
}

.el-table>>>.part8-row {
  color: white;
  background: rgb(41, 83, 117) !important;
}

.el-table>>>.part9-row {
  color: white;
  background: rgb(57, 134, 122) !important;
}

.el-table>>>.part10-row {
  color: black;
  background: rgb(251, 255, 0) !important;
}

.el-table>>>.part11-row {
  color: black;
  background: rgb(0, 255, 234) !important;
}

.el-table>>>.green-row {
  font-family: CommitMono;
  font-size: 13px;
  background: rgb(24, 204, 0) !important;
}

.el-table>>>.greensmall-row {
  font-family: CommitMono;
  font-size: 13px;
  background: rgba(113, 255, 113, 0.705) !important;
}

.el-table>>>.redsmall-row {
  font-family: CommitMono;
  font-size: 13px;
  background: rgb(255, 166, 166) !important;
}

.el-table>>>.normal-row {
  font-family: CommitMono;
  font-size: 13px;
}

.textcon {
  width: 100vw;
  display: flex;
  justify-content: center;
  flex-direction: row;
}

.textconin {
  width: 80%;
  height: 80%;
  overflow: hidden;
}
</style>