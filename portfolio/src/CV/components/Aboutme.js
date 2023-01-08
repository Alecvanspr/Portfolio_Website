import React from "react";
import picture from "../components/me.JPG";


const Aboutme = ({
}) => (
    <>
    <div className="container position-relative py-lg-6 py-5">
        <div className="row">
        <h2 className="display-4 mb-0 text-white">Be part of the <span className="d-block font-weight-bold">Lunar XPerience</span></h2>
        <p className="lead my-4 text-white">If you're an explorer, then the moon is calling.<br/>
        Join the LunarXP mission where new worlds await.</p>
        <div className="spacer"></div>
        </div>
        <div className="position-absolute left-0 w-100 text-center d-md-block image-container">
            <img id='blur' className="img-fluid heroImage" src={picture}/>
        </div>
    </div>
    <div className="card justify-contents">
      <h1 className="text-center">Alec van Spronsen</h1>
    </div>
    </>
)

export default Aboutme;