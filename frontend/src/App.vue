<template>
  <el-backtop :right="100" :bottom="100" />
    <div class="title-container">
      <el-row style="display: flex; justify-content: center; align-items: center;">
        <el-col>
          <h1 style="color:#fff; text-align:center">{{ this.title }}</h1>
        </el-col>
      </el-row>

      <el-row style="margin-bottom: 15px; display: flex; justify-content: center; align-items: center;">
        <el-col :span="20">
          <el-progress :percentage="time_percentage" :show-text="false" :stroke-width="20" :color = "status_text == '进行中' ? 'green':'red'"
          striped striped-flow :duration="50"></el-progress>
        </el-col>
      </el-row>

      <el-row style="margin-bottom: 15px; display: flex; justify-content: center; align-items: center">
        <el-row style="margin-bottom: 15px;">
          <div style="width: 22px; height: 22px; border-radius: 50%;" :class="{ 'green': status_text == '进行中', 'red': status_text == '已结束' }"></div>
        </el-row>
        <el-row style="margin-bottom: 17px; margin-left: 10px;">
          <div style="text-align:center; font-size: 20px; font-weight: bold;">{{ status_text }}  {{ time_string }}</div>
        </el-row>
      </el-row>
    </div>
    <el-menu router class="menu-main" active-text-color="rgb(0, 238, 255)" :default-active="activeMenu" mode="horizontal" @select="handleMenuSelect">
      <el-menu-item index="/teams_ranking">
        <el-icon><WindPower /></el-icon>
        <span class="menu-item">团队排名</span>
      </el-menu-item>
      <el-menu-item index="/students_ranking">
        <el-icon><UserFilled /></el-icon>
        <span class="menu-item">个人排名</span>
      </el-menu-item>
    </el-menu>
    <router-view></router-view>
</template>

<script>
import axios from 'axios';
export default {
  name: 'App',
  data() {
    return {
      activeMenu: '/students_ranking',
      startTime: null,
      endTime: null,
      time_percentage: 0,
      time_string: null,
      status_text: null,
      title: null,
    };
  },
  created() {
    this.activeMenu = this.$route.path;
    this.fetchCompetitionTitle();
    this.fetchCompetitionTimes();
  },
  unmounted() {
    this.clearTimer();
  },
  watch: {
    '$route'(to, from) {
      this.activeMenu = to.path;
    },
  },
  methods: {
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    // 格式化时间，保证时、分、秒都是两位数
    formatTime(value) {
      return value < 10 ? `0${value}` : value;
    },

    progressPercentage() {
      const currentTime = new Date().getTime();
      const totalTime = this.endTime - this.startTime;
      const elapsedTime = currentTime - this.startTime;
      // 防止超出范围
      this.time_percentage = Math.min((elapsedTime / totalTime) * 100, 100);
    },

    // 计算比赛剩余时间的倒计时
    countdownTime() {
      const remainingTime = Math.max(this.endTime - new Date().getTime(), 0);
      const hours = Math.floor(remainingTime / (60 * 60 * 1000));
      const minutes = Math.floor((remainingTime % (60 * 60 * 1000)) / (60 * 1000));
      const seconds = Math.floor((remainingTime % (60 * 1000)) / 1000);
      this.time_string = `${this.formatTime(hours)}:${this.formatTime(minutes)}:${this.formatTime(seconds)}`;
    },

    // 计算比赛状态
    competitionStatus() {
      const local_time = new Date().toLocaleString();
      const currentTime = new Date(local_time).getTime();
      if (currentTime < this.startTime) {
        return "未开始";
      } 
      else if (currentTime >= this.startTime && currentTime <= this.endTime) {
        return "进行中";
      } 
      else {
        return "已结束";
      }
    },

    // 获取比赛状态文本
    statusText() {
      this.status_text = this.competitionStatus();
    },

    // 获取比赛时间数据
    fetchCompetitionTimes() {
      axios.get('http://101.133.228.198:3000/competition/time')
        .then(response => {
          const start_to_local = new Date(response.data[0].Start_time).toLocaleString();
          const end_to_local = new Date(response.data[0].End_time).toLocaleString();
          this.startTime = new Date(start_to_local).getTime();
          this.endTime = new Date(end_to_local).getTime();
          // 启动倒计时更新
          this.updateCountdown();
        })
        .catch(error => {
          console.error('Error fetching competition times:', error);
        });
    },

    fetchCompetitionTitle() {
      axios.get('http://101.133.228.198:3000/competition/data')
        .then(response => {
          this.title = response.data[0].Title;
        })
        .catch(error => {
          console.error('Error fetching competition times:', error);
        });
    },
    // 更新倒计时
    updateCountdown() {
      setInterval(() => {
        // 通过 setInterval 每秒更新一次倒计时
        if (this.endTime > new Date().getTime()) {
          this.statusText();
          this.countdownTime();
          this.progressPercentage();
          this.$forceUpdate();
        }
        else{
          this.statusText();
          this.time_string = '00:00:00';
          this.time_percentage = 100;
          this.$forceUpdate();
        }
      }, 1000);
    },
    clearTimer() {
      if (this.timer) {
        clearInterval(this.timer);
      }
    },
  },
};
</script>

<style>
body, html {
  margin: 0;
  padding: 0;
  background-image: url('./assets/Images/back.jpg');
  background-size: repeat;
}

.title-container {
  width: 100%;
  backdrop-filter: blur(10px);
  background-color: #22222227;
}

.menu-main {
  display: flex;
  width: 100%;
  justify-content: center;
  .el-menu-item:hover,
  .el-menu-item:focus{
    backdrop-filter: blur(2px);
    background-color: #97979754 !important;
    --el-menu-hover-text-color:rgb(0, 238, 255);
  }
  .el-menu-item.is-active {
    backdrop-filter: blur(2px);
    background-color: #62626243; /* 设置焦点背景色 */
  }
}

.menu-item {
  font-size: 20px;
}

.countdown {
  font-size: 24px;
  color: #c7c7c7;
}

.status-circle {
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.green {
  background-color: green;
}

.red {
  background-color: red;
}

.status-text {
  font-size: 18px;
}
</style>