import React, { Component } from "react";
import Aboutme from "../components/Aboutme";
import JobComponent from "../components/JobComponent";
import axios from "axios";

class CVContainer extends Component {
  constructor(props) {
    super(props)
    this.state = {
      jobs:[]
    }
  }
  componentDidMount() {
    this.refreshList()
  }

  refreshList = () => {
    axios
      .get("api/job/")
      .then(res => this.setState({ jobs: res.data }))
      .catch(err => console.log(err));
  }

  render() {
    const {jobs} = this.state
    return (
      <div className="mt-4">
        {jobs.map((job)=> (<JobComponent job={job}/>))}
      </div>
    );
  }
}

export default CVContainer;