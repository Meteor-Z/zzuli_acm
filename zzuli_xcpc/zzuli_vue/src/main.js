import { createApp } from 'vue';
import App from './App.vue';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'
// import 'element-plus/theme-chalk/dark/css-vars.css';
import * as ElementPlusIconsVue from '@element-plus/icons-vue';
import { createRouter, createWebHistory } from 'vue-router';
import StudentTable from './components/student-rank.vue';
import './assets/Fonts/font.css';
// import ManagerView from './components/manager-view.vue';

const app = createApp(App);
const routes = [
    { path: '/', redirect: '/students_ranking' },
    { path: '/students_ranking', component: StudentTable },
    // { path: '/zzulirank_manager', component: ManagerView },
];
const router = createRouter({
    history: createWebHistory(),
    routes,
});

app.use(ElementPlus);
app.use(router);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.mount('#app');