import { Container } from '@mui/system';
import { Grid, Divider, Box, Button } from '@mui/material';
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import {getStudyRoom} from '../../store/CheckedSlice';
import EditOutlinedIcon from '@mui/icons-material/EditOutlined';
import DeleteOutlinedIcon from '@mui/icons-material/DeleteOutlined';
import deleteArticle from '../../components/modals/DeleteArticle';




function ArticleDetail() {

	const dispatch = useDispatch();
	const navigate = useNavigate();
  const article = useSelector(state => {
		return state.checkDays
	});

	const [day, setDay] = useState("");
	const [studyPlan, setStudyPlan] = useState("");

	useEffect(() => {
		let date = ""
		for (let i = 0; i < article.day.length; i++) {
			if (article.day[i] === "1")	{
				if (i === 0)	{
					date = date + "월"
				}	else if (i === 1)	{
					date = date + "화"
				}	else if (i === 2)	{
					date = date + "수"
				}	else if (i === 3)	{
					date = date + "목"
				}	else if (i === 4) {
					date = date + "금"
				}	else if (i === 5) {
					date = date + "토"
				}  else if (i === 6) {
					date = date + "일"
        }
			}
		setDay(date)
		}

		if (article.beginAt === "" || article.endAt === "") {
			setStudyPlan("미정")
		}	else	{
			setStudyPlan(article.beginAt + " ~ " + article.endAt)
		}
	}, [article.day])

	useEffect(() => {
		// 글이 지워졌을때 보드로 돌아가는 함수
		if (article.title === "") {
			navigate("/group/board")
		}
	}, [])

	
	 
  return (
		<>
			<Container sx={{ border: "1px gray solid", borderRadius: "10px", minWidth: "1000px"}}>
				<Grid container sx={{ px: 2 }}>
					<Grid item xs={6} sx={{ display: "flex", alignItems: "center", justifyContent: ""}}>
    				<p style={{ fontWeight: "bold", fontSize: "30px"}}>
							<span style={(article.category === "스터디") ? { color: "red" } : { color: "blue" }}>[{article.category}]</span>
							<span style={{ marginLeft: 30 }}>{article.title}</span>
						</p>
						<p style={{ paddingLeft: 30, paddingTop: 5}}>
							<EditOutlinedIcon
								variant="contained"
								sx={{ fontSize: 30, color: "blue" }}
								onClick={() => {navigate("/group/board/:boardId/update")}} />
						</p>
						<p style={{ paddingLeft: 10, paddingTop: 5}}>
							<DeleteOutlinedIcon
								onClick={deleteArticle}
								sx={{ fontSize: 30, color: "red" }} 
							/>
						</p>
					</Grid>
					<Grid item xs={3}>
					</Grid>
					<Grid item xs={1.5} sx={{ alignItems: "center", display: "flex", pl: 5}}>
					</Grid>
					<Grid item xs={1.5} sx={{ alignItems: "center", display: "flex", pl: 4}}>
						<Button 
							variant="contained" 
							sx={{ height: "40px" }} 
							onClick={() => {
								dispatch(getStudyRoom())							
								navigate("/group/board");
								}}>목록 보기</Button>
					</Grid>
				</Grid>
				<Grid container>
					<Grid item xs={1} sx={{ textAlign: "center" }}>
						<p>서형준</p>
					</Grid>
					<Grid item xs={8} sx={{ px: 3 }}>
						<p>{article.writedAt}</p>
					</Grid>
					<Grid item xs={3} sx={{ textAlign: "right", display: "flex", justifyContent: "right", pr: 3 }}>
						<p>조회수 : 6</p>
					</Grid>
				</Grid>
				<Divider orientation='horizontal' flexItem sx={{ borderBottomWidth: 5 }}/>
				<Grid container>
					<Grid item xs={2} sx={{ alignContent: "center" }}>
						<p style={{ fontWeight: "bold", textAlign: "center" }}>스터디 일정</p>
					</Grid>
					<Grid item xs={3}>
						<p>{studyPlan}</p>
					</Grid>
					<Divider orientation='vertical' flexItem variant='middle' sx={{ mr: 2 }}/>
					<Grid item xs={2}>
						<p style={{ fontWeight: "bold", textAlign: "center" }}>스터디 시간</p>
					</Grid>
					<Grid item xs={2}>
						<p style={{ textAlign: "center" }}>{day} {article.startTime} - {article.finishTime}</p>
					</Grid>
					<Divider orientation='vertical' flexItem variant='middle' sx={{ mx: 2 }}/>
					<Grid item xs={1}>
						<p style={{ fontWeight: "bold", textAlign: "center" }}>인원 현황</p>
					</Grid>
					<Grid item xs={1}>
						<p style={{ textAlign: "center" }}>3 / {article.recruitmentNumber}</p>
					</Grid>
				</Grid>
				<Grid container>
					<Grid item xs={2} sx={{ alignContent: "center" }}>
						<p style={{ fontWeight: "bold", textAlign: "center" }}>상세 내용</p>
					</Grid>
				</Grid>
				<Container 
					sx={{ width: "85%", minHeight: "500px", borderRadius: "10px", backgroundColor: "rgba(244, 239, 230, 0.47)", padding: 3, mb: 3}}>
					<Box>
						<div style={{ whiteSpace: "pre-wrap", paddingLeft: 10, paddingTop: 10, overflowY: "scroll", height: "500px" }}>{article.content}</div>
					</Box>
				</Container>
			</Container>
		</>
  )
}

export default ArticleDetail