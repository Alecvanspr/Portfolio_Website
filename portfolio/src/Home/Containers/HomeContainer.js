import React, { Component } from "react";
import { Container } from "reactstrap";
import '../Home.css'

class HomeContainer extends Component {
    constructor(props){
        super(props)
        this.state ={

        }
    }
    render(){

        return(
            <>
                <div className="">
                    <div className="fixed-bg">
                    </div>
                </div>
                <div className="">
                    <div className="profile-picture"/>
                    <div className="dark-blue buffer"><p className="h1">Alec van Spronsen</p></div>
                    <div className="light-blue buffer"><p className="h3">Student software engineer</p> </div>
                </div>

            </>
        
        )
    }
}
export default HomeContainer;