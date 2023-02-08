import React, { useEffect, useState } from "react";
import Card from "@mui/material/Card";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import OpenViduApp from "../OpenVidu/OpenViduApp";
import MyTodo from "../MyPageReport/MyTodo";
import MyTime from "../MyPageReport/MyTime";
import NSRoomCard from "./RoomScroll/NSRoomCard";
import FTRoomCard from "./RoomScroll/FTRoomCard";

import { Box } from "@mui/material";
import IconButton from "@mui/material/IconButton";
import Grid from "@mui/material/Grid";
import { LeftArrow, RightArrow } from "./RoomScroll/Arrows";
import usePreventBodyScroll from "./RoomScroll/usePreventBodyScroll";
import { ScrollMenu, VisibilityContext } from "react-horizontal-scrolling-menu";

import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";

import axios from "axios";
import RoomInfo from "./RoomScroll/RoomInfo";
import NavBar from "../../components/NavBar/NavBar";

import "./RoomScroll/hideScrollbar.css";
import { resolveComponentProps } from "@mui/base";

// const getrooms = () =>
//   Array(1) //카드의 개수 추정 0부터 10까지 있는 카드
//     .fill(0)
//     .map((_, ind) => ({ id: `element-${ind}` }));

function StudyRoomMain() {
  const [rooms, setrooms] = useState([]);
  const [noRooms, setnoRooms] = useState([]); //nonstop방만 저장할 배열
  const [yesRooms, setyesRooms] = useState([]); //쉬는시간방만 저장할 배열

  const Token =
    "eyJyZWdEYXRlIjoxNjc1NzQ0NzMwMTU0LCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzdHJpbmdAZ21haWwuY29tIiwiZXhwIjoxNjc1ODMxMTMwLCJlbWFpbCI6InN0cmluZ0BnbWFpbC5jb20iLCJtZW1iZXJJZCI6ODN9.QCvJ0J6OvsmxkiqrYQSWhUjOpdrbVzrWSZNO4q0Bahs";

  useEffect(() => {
    axios({
      method: "get",
      url: "http://i8a302.p.ssafy.io:8081/studyrooms",
      headers: {
        Authorization: `Bearer ${Token}`,
      },
    }).then((res) => {
      // console.log(res.data);
      console.log(res.data.publics);

      if ("success_get_studyrooms") {
        setrooms(res.data.publics);
        // console.log(res.data.publics);
      } else {
      }
    });
  }, []);
  console.log(rooms);
  useEffect(() => {
    const NR = rooms.filter((room) => room.type === "N");
    setnoRooms(NR);
    console.log(noRooms);
    const YR = rooms.filter((room) => room.type === "Y");
    setyesRooms(YR);
  }, [rooms]);

  // const navigate = useNavigate();

  //방 추가하는 함수, 추가하고 바로 이동
  const addItem = (typeOfRoom) => {
    console.log(typeOfRoom);

    if (typeOfRoom === "Y") {
      axios({
        method: "post",
        url: "http://i8a302.p.ssafy.io:8081/studyrooms",
        headers: { Authorization: `Bearer ${Token}` },
        body: { type: "Y" },
      }).then((res) => {
        console.log(res);
        // console.log(res.data.publics);
        console.log("i need a room id Y");
      });

      //방 입장하는 axios 이어서 작성 필요
    } else if (typeOfRoom === "N") {
      axios({
        method: "post",
        url: "http://i8a302.p.ssafy.io:8081/studyrooms",
        headers: { Authorization: `Bearer ${Token}` },
        body: { type: "N" },
      }).then((res) => {
        console.log(res.data.publics);
        console.log("i need a room id N");
      });
    }
  };

  /////로컬 스토리지 실험중//////
  //로컬 스토리지에 시간 초기화하는 코드 일단 넣고,
  //오픈비두 입장버튼 눌렀을 때에 입장 시간 저장 필요

  return (
    <>
      <NavBar />
      <Box
        sx={{
          flexGrow: 1,
          color: "text.secondary",
          marginTop: 8,
          height: "100vh",
          bgcolor: "#1A1E33F2",
          position: "static",
          // overscrollBehavior: "contain",
        }}
      >
        {/* 하나 xs 값 주면 나머지 알아서*/}
        <Grid container>
          {/* 그리드 컴포넌트 사이 넓이 */}
          <Grid item xs={3} style={{}}>
            {/* todo& 목표 공부시간 묶는 div */}
            <Grid
              item
              xs={8}
              sx={{ marginTop: 3, marginX: "auto", paddingLeft: "20px" }}
            >
              <Typography
                variant="h5"
                sx={{ fontSize: 20, color: "white", marginTop: 2 }}
              >
                Todo List
              </Typography>
              <Grid
                item
                xs={11}
                sx={{
                  backgroundColor: "#F4EFE6",
                  borderRadius: 2,
                  paddingX: "10px",
                }}
              >
                <MyTodo />
              </Grid>
            </Grid>
            <Grid item xs={8} sx={{ marginX: "auto", paddingLeft: "20px" }}>
              {/* 목표 공부시간 div */}
              <Typography
                variant="h5"
                sx={{
                  fontSize: 20,
                  color: "white",
                  marginTop: 2,
                  marginBottom: -2,
                }}
              >
                목표 공부 시간
              </Typography>
              <Grid
                item
                xs={11}
                sx={{
                  backgroundColor: "#F4EFE6",
                  borderRadius: 2,
                  paddingX: "10px",
                }}
              >
                <MyTime />
              </Grid>
            </Grid>
          </Grid>
          <Grid
            item
            xs={9}
            style={{
              position: "relative",
              displayPrint: "inline-block",
              marginTop: "0%",
              marginLeft: "0%",
            }}
          >
            <Grid item xs={12}>
              <Typography
                variant="h1"
                sx={{ fontSize: 30, color: "white", marginTop: 2 }}
              >
                STUDY ROOM
              </Typography>
            </Grid>
            <Grid container>
              <Grid
                item
                xs={11.2}
                style={{
                  position: "relative",
                  // displayPrint: "inline-block",
                  // backgroundColor: "green",
                }}
              >
                <ScrollMenu
                  // LeftArrow={LeftArrow} //좌우 클릭으로 이동
                  // RightArrow={RightArrow}
                  onWheel={onWheel}
                >
                  <RoomInfo />
                  {noRooms.map((room, i) => (
                    <>
                      <NSRoomCard
                        key={i}
                        id={room.id}
                        sessionName={room.session_name}
                        partici={room.count}
                      />
                    </>
                  ))}
                </ScrollMenu>
              </Grid>
              <Grid
                item
                xs={0.8}
                style={{
                  position: "relative",
                  display: "inline-block",
                  // backgroundColor: "yellow",
                }}
              >
                <IconButton
                  onClick={() => {
                    addItem("N");
                  }}
                  sx={{ color: "white", top: "45%", width: "80px" }}
                >
                  <AddCircleOutlineIcon />
                </IconButton>
              </Grid>
            </Grid>
            <Grid container sx={{ marginTop: "2%" }}>
              <Grid
                item
                xs={11.2}
                style={{
                  position: "relative",
                  displayPrint: "inline-block",
                  // backgroundColor: "red",
                  // marginTop: "2%",
                  height: "100%",
                }}
              >
                <ScrollMenu
                  // LeftArrow={LeftArrow}
                  // RightArrow={RightArrow}
                  onWheel={onWheel}
                >
                  {yesRooms.map((room) => (
                    <>
                      <FTRoomCard
                        key={room.id}
                        id={room.id}
                        sessionName={room.session_name}
                        partici={room.count}
                      />
                    </>
                  ))}
                </ScrollMenu>
              </Grid>
              <Grid
                item
                xs={0.8}
                style={{
                  position: "relative",
                  displayPrint: "inline-block",
                  position: "relative",
                }}
              >
                <IconButton
                  onClick={() => {
                    addItem("Y");
                  }}
                  sx={{ color: "white", top: "45%", width: "80px" }}
                >
                  <AddCircleOutlineIcon />
                </IconButton>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Box>
    </>
  );
}

export default StudyRoomMain;

function onWheel(apiObj, ev) {
  const isThouchpad = Math.abs(ev.deltaX) !== 0 || Math.abs(ev.deltaY) < 15;

  if (isThouchpad) {
    ev.stopPropagation();
    return;
  }

  if (ev.deltaY < 0) {
    apiObj.scrollNext();
  } else if (ev.deltaY > 0) {
    apiObj.scrollPrev();
  }
}
