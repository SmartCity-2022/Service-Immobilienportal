import React, { useEffect, useState } from "react";
import './App.css';

const App = () => {
  const [message, setMessage] = useState("");

  const getMsg = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type" : "application/json",
      },
    };
    const response = await fetch("/api", requestOptions);
    const data = await response.json();

    if(!response.ok){
      console.log("Something went wrong...");
    }else{
      setMessage(data.message);
    }
  };

  useEffect(() => {
    getMsg();
  }, []);
  return (
    <div>
      <h1> {message} </h1>
    </div>
  );
}

export default App;
