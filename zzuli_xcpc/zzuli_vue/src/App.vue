<template>
  <div class="banner">
    <img class="bannerimg" src="./assets/Images/banner.png" alt="banner">
  </div>
  <div class="textcon">
    <div style="width:92%; display:block">
      <div style="display: flex; font-family: CommitMono;"><!-- 第一行标签容器 -->
        <div float="left" style="display:block;">
          <p>Starting From：{{this.startTime_str}} <sup>GMT+8</sup></p>
        </div>
        <div style="flex:1 1 0%; display:block;">
          <div style="display: flex; flex-direction: row; align-items: center; justify-content: center;">
            <div v-if="competitionStatus == `WAITING`"
              style="display:inline-block; width: 14px; height: 14px; border-radius: 50%;" class="gray"></div>
            <div v-if="competitionStatus == `FINISHED`"
              style="display:inline-block; width: 14px; height: 14px; border-radius: 50%;" class="red"></div>
            <div v-if="competitionStatus == `RUNNING`"
              style="display:inline-block; width: 14px; height: 14px; border-radius: 50%;" class="green"></div>
            <p style="display:block; font-size: 18px;">{{ competitionStatus }}</p>
          </div>
        </div>
        <div class="textrow" float="right" style="display:inline-block;">
          <p>Close At：{{this.endTime_str}} <sup>GMT+8</sup></p>
        </div>
      </div>
      <div class="progress-container">
        <div class="progress-bar" :style="{ 'width': bar_val + '%' }"></div>
      </div>
      <div style="display: flex; font-family: CommitMono;"><!-- 第一行标签容器 -->
        <div float="left" style="display:block;">
          <p>Elapsed Time： {{passingTime}}</p>
        </div>
        <div style="flex:1 1 0%; display:block;">
          <div style="display: flex; flex-direction: row; align-items: center; justify-content: center;">
          </div>
        </div>
        <div class="textrow" float="right" style="display:inline-block;">
          <p>Remain Time：{{remainingTime}}</p>
        </div>
      </div>
    </div>
  </div>
  <router-view></router-view>
</template>

<script>
import axios from 'axios';
import ref from 'vue';
import getConfig from '../config';
export default {
  name: 'App',
  data() {
    return {
      apiconfig: getConfig(),
      activeMenu: '/students_ranking',
      startTime: null,
      endTime: null,
      startTime_str: null,
      endTime_str: null,
      status_text: null,
      title: null,
      networkTime: null,
      bar_val: 0,
    };
  },
  created() {
    this.activeMenu = this.$route.path;
    this.fetchCompetitionTitle();
    this.fetchCompetitionTimes();
  },
  watch: {
    '$route'(to, from) {
      this.activeMenu = to.path;
    },
  },
  computed: {
    remainingTime() {
      const remainTime = Math.max(this.endTime - this.networkTime, 0);
      const hours = Math.floor(remainTime / (60 * 60 * 1000));
      const minutes = Math.floor((remainTime % (60 * 60 * 1000)) / (60 * 1000));
      const seconds = Math.floor((remainTime % (60 * 1000)) / 1000);
      if(this.networkTime >= this.startTime){
        return `${this.formatTime(hours)}:${this.formatTime(minutes)}:${this.formatTime(seconds)}`;
      }
      else{
        return `WAITING START`;
      }
    },
    passingTime() {
      const remainTime = Math.max(this.networkTime - this.startTime, 0);
      const hours = Math.floor(remainTime / (60 * 60 * 1000));
      const minutes = Math.floor((remainTime % (60 * 60 * 1000)) / (60 * 1000));
      const seconds = Math.floor((remainTime % (60 * 1000)) / 1000);
      if(this.networkTime >= this.startTime){
        return `${this.formatTime(hours)}:${this.formatTime(minutes)}:${this.formatTime(seconds)}`;
      }
      else{
        return `WAITING START`;
      }
    },
    progressPercentage() {
      const currentTime = this.networkTime;
      const totalTime = this.endTime - this.startTime;
      const elapsedTime = currentTime - this.startTime;
      if (currentTime < this.startTime) {
        return 0;
      }
      else{
        return Math.min((elapsedTime / totalTime) * 100, 100);
      }
    },
    competitionStatus() {
      const currentTime = this.networkTime;
      if (currentTime < this.startTime) {
        return "WAITING";
      }
      else if (currentTime >= this.startTime && currentTime <= this.endTime) {
        return "RUNNING";
      }
      else {
        return "FINISHED";
      }
    },
  },
  unmounted() {
    this.clearTimer();
  },
  methods: {
    formatTime(value) {
      return value < 10 ? `0${value}` : value;
    },

    getNetworkTime() {
      const temp = new Date().toLocaleString();
      this.networkTime = new Date(temp).getTime();
    },

    fetchCompetitionTimes() {
      axios.get(`${this.apiconfig.apiUrl}/competition/time`)
        .then(response => {
          this.startTime_str = response.data[0].Start_time;
          this.endTime_str = response.data[0].End_time;
          const s1 = new Date(this.startTime_str);
          const s2 = new Date(this.endTime_str);
          this.startTime = new Date(s1).getTime();
          this.endTime = new Date(s2).getTime();
          this.updateCountdown();
        })
        .catch(error => {
          console.error('Error fetching competition times:', error);
        });
    },

    fetchCompetitionTitle() {
      const apiconfig = import('../config');
      axios.get(`${this.apiconfig.apiUrl}/competition/data`)
        .then(response => {
          this.title = response.data[0].Title;
        })
        .catch(error => {
          console.error('Error fetching competition title:', error);
        });
    },

    updateCountdown() {
      setInterval(() => {
        this.getNetworkTime();
        this.bar_val = this.progressPercentage;
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
body,
html {
  margin: 0;
  padding: 0;
  background-size: repeat;
}

.banner {
  display: flex;
  justify-content: center;
}

.bannerimg {
  width: auto;
  height: auto;
  max-width: 80%;
  max-height: 80%;
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

.green {
  background-color: green;
}

.red {
  background-color: red;
}

.gray {
  background-color: rgb(77, 77, 77);
}

.progress-container {
  width: 100%;
  background-color: #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar {
  height: 15px;
  background-color: #66ccff;
  transition: width 1s ease-in-out;
  border-radius: 4px;
  background-image: linear-gradient(45deg, #7474743f 25%, transparent 25%, transparent 50%, #7e7e7e50 50%, #a1a1a13f 75%, transparent 75%, transparent);
  background-size: 40px 40px;
  animation: progressAnimation 2s infinite linear;
}
@keyframes progressAnimation {
  0% {
    background-position: 0 0;
  }
  100% {
    background-position: 40px 0;
  }
}
</style>