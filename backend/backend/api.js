const express = require('express');
const mysql = require('mysql');
const cors = require('cors');
const app = express();
app.use(cors());

const connection = mysql.createConnection({
    host: 'zzulirank-mysql',
    user: 'root',
    port: 3306,
    password: 'mysqlpassword',
    database: 'PTA_Data',
    multipleStatements: true,
    autocommit: false,
});
connection.connect();
module.exports = connection;

setInterval(() => {
    connection.query('SELECT 1', (err, results) => {
        if (err) console.error(err);
    });
}, 60000);

app.post('/competition/set_standard/:s1/:s2/:s3', (req, res) => {
    const standard1 = req.params.s1;
    const standard2 = req.params.s2;
    const standard3 = req.params.s3;
    const query = `UPDATE Competition_Info SET standard1 = ${standard1},standard2 = ${standard2},standard3 = ${standard3}`;
    connection.query(query, (error, results) => {
        if (error) {
            res.json({ message: 'error' });
            console.log(error);
        } else {
            res.json({ message: 'success' });
            console.log('Scores updated successfully:', results);
        }
    });
});

app.post('/competition/set_title/:string', (req, res) => {
    const title = req.params.string;
    const query = `UPDATE Competition_Info SET Title = "${title}"`;
    connection.query(query, (error, results) => {
        if (error) {
            res.json({ message: 'error' });
            console.log(error);
        } else {
            res.json({ message: 'success' });
            console.log('Title updated successfully:', results);
        }
    });
});

app.post('/competition/set_pta/:session/:problem_set', (req, res) => {
    const Session = req.params.session;
    const Problem_set = req.params.problem_set;
    const query = `UPDATE Competition_Info SET PTA_session = "${Session}",Problem_Set = "${Problem_set}"`;
    connection.query(query, (error, results) => {
        if (error) {
            res.json({ message: 'error' });
            console.log(error);
        } else {
            res.json({ message: 'success' });
            console.log('PTA_Data updated successfully:', results);
        }
    });
});

app.get('/competition/data', (req, res) => {
    const query = `SELECT * FROM Competition_Info`;
    connection.query(query, (error, results) => {
        if (error) {
            console.log(error);
        }
        res.json(results);
    });
});

app.get('/competition/time', (req, res) => {
    const query = `SELECT Start_time,End_time FROM Competition_Info`;
    connection.query(query, (error, results) => {
        if (error) {
            console.log(error);
        }
        res.json(results);
    });
});

app.get('/competition/standard', (req, res) => {
    const query = `SELECT standard1,standard2,standard3 FROM Competition_Info`;
    connection.query(query, (error, results) => {
        if (error) {
            console.log(error);
        }
        res.json(results);
    });
});

app.get('/students', (req, res) => {
    const query = `SELECT * FROM Student_Info ORDER BY rank ASC`;
    connection.query(query, (error, results) => {
        if (error) {
            console.log(error);
        }
        res.json(results);
    });
});

app.get('/students/students_by_stuid/:stuID', (req, res) => {
    const stuid = req.params.stuID;
    const query = `SELECT * FROM Student_Info WHERE stu_id = ${stuid}`;
    connection.query(query, (error, results) => {
        if (error) {
            console.log(error);
        }
        res.json(results);
    });
});

app.get('/students/students_by_id/:teamID', (req, res) => {
    const teamid = req.params.teamID;
    const query = `SELECT * FROM Student_Info WHERE team_id = ${teamid} ORDER BY rank ASC`;
    connection.query(query, (error, results) => {
        if (error) {
            console.log(error);
        }
        res.json(results);
    });
});

app.get('/students/total-count', (req,res) => {
    const query = 'SELECT COUNT(*) as totalCount FROM Student_Info';
    connection.query(query, (error, results) => {
        if (error) {
            console.log(error);
        }
        const totalCount = results[0].totalCount;
        res.json({ totalCount });
    });
});

app.get('/teams', (req, res) => {
    const query = `SELECT * FROM Team_Info ORDER BY rank ASC`;
    connection.query(query, (error, results) => {
        if (error) {
            console.log(error);
        }
        res.json(results);
    });
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});