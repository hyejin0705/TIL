import React, { useState } from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import TextField from "@mui/material/TextField";
import DialogTitle from "@mui/material/DialogTitle";
import { Box, Grid, IconButton, Typography } from "@mui/material";
import ModeEditOutlineOutlinedIcon from "@mui/icons-material/ModeEditOutlineOutlined";

function MyInfo() {
  const [name, setName] = useState("김싸피");
  const [email, setEmail] = useState("ksf@gmail.com");
  const [pw, setPw] = useState("123456");

  //각각 개인정보 수정 모달/탈퇴 확인 모달 열고 닫는 상태 useState
  const [infoUpdateMOpen, setInfoUpdateMOpen] = useState(false);
  const [quitMOpen, setQuitMOpen] = useState(false);

  //개인정보 수정 모달 열고 닫는 함수
  const iumClickOpen = () => {
    setInfoUpdateMOpen(true);
  };

  const iumClose = () => {
    setInfoUpdateMOpen(false);
  };

  //탈퇴 모달 열고 닫는 함수
  const qmClickOpen = () => {
    setQuitMOpen(true);
  };

  const qmClose = () => {
    setQuitMOpen(false);
  };

  return (
    <>
      <Box
        sx={{
          width: 420,
          height: 350,
          backgroundColor: "white",
          borderRadius: 2,
          padding: "10px",
          boxShadow: "2px 2px 7px 1px grey",
        }}
      >
        <Grid container>
          <Grid item xs={3}>
            <h3 style={{ marginLeft: "15px" }}>내 정보</h3>
          </Grid>
          <Grid item xs={3} sx={{ marginLeft: "50%" }}>
            <IconButton
              color="#3A3A3A"
              aria-label="modify"
              onClick={iumClickOpen}
              sx={{ marginLeft: "50%", marginTop: "10px" }}
            >
              <ModeEditOutlineOutlinedIcon />
            </IconButton>
          </Grid>
        </Grid>
        <hr />
        <Grid container sx={{ marginLeft: "10%", marginTop: "5%" }}>
          <Grid container sx={{ marginY: "10%" }}>
            <Grid item xs={3}>
              <Typography variant="body1">닉네임</Typography>
            </Grid>
            <Grid item xs={8}>
              <Typography variant="body1">{name}</Typography>
            </Grid>
          </Grid>
          <Grid container>
            <Grid item xs={3}>
              <Typography variant="body1">이메일</Typography>
            </Grid>
            <Grid item xs={8}>
              <Typography variant="body1">{email}</Typography>
            </Grid>
          </Grid>
        </Grid>
        <Grid xs={12}>
          <Button
            variant="text"
            sx={{ color: "#A9A9A9", marginLeft: "80%", marginTop: "17%" }}
            onClick={qmClickOpen}
          >
            탈퇴하기
          </Button>
        </Grid>
      </Box>

      <Dialog open={infoUpdateMOpen} onClose={iumClose}>
        <DialogTitle>내 정보 수정</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            fullWidth
            margin="dense"
            id="outlined-helperText"
            label="닉네임"
            defaultValue={name}
          />
          <TextField
            autoFocus
            fullWidth
            id="outlined-disabled"
            label="email"
            defaultValue={email}
            InputProps={{
              readOnly: true,
            }}
          />
          <TextField
            autoFocus
            fullWidth
            id="outlined-required"
            label="현재 비밀번호"
            defaultValue=""
          />
          <TextField id="outlined-helperText" label="Helper text" defaultValue="Default Value" />
          <TextField id="outlined-helperText" label="비밀번호 확인" defaultValue="" />
        </DialogContent>
        <DialogActions>
          <Button onClick={iumClose}>Save</Button>
          <Button onClick={iumClose}>Cancel</Button>
        </DialogActions>
      </Dialog>

      <Dialog
        open={quitMOpen}
        onClose={qmClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"정말 탈퇴하시겠습니까?"}</DialogTitle>
        <DialogActions>
          <Button onClick={qmClose}>Disagree</Button>
          <Button onClick={qmClose} autoFocus>
            Agree
          </Button>
        </DialogActions>
      </Dialog>
    </>
  );
}

export default MyInfo;
