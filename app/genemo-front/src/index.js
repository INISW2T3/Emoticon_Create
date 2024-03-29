import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { Header, FormWizard} from "./App";
//import FormWizard  from "./Wizard";
import reportWebVitals from "./reportWebVitals";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <Header />
    <FormWizard />
  </React.StrictMode>
);

reportWebVitals();
