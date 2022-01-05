import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage"
import Login from "./Login"
import Signup from "./Signup"
import UserDash from "./UserDash"
import WritePost from "./WritePost"
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Redirect
  } from "react-router-dom";
export const App = () => {
return(
    <Router>
        <Routes>
        <Route exact path="/" element={<HomePage />} />
        <Route path="/Login" element={<Login />} />
        <Route path="/Signup" element={<Signup />} />
        <Route path="/UserDash" element={<UserDash />} />
        <Route path="/WritePost" element={<WritePost />} />
        </Routes>
    </Router>
)
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);