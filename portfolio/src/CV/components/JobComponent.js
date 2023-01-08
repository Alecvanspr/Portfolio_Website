import React from "react";

const JobComponent = ({job}) => {
  const {
    id,
    title,
    company,
    location,
    start_date,
    end_date,
    description,
    image,
    website,
  } = job
  return(
    <div className="card justify-contents" id={id}>
      <h1 className="text-center">{title}</h1>
      <small className="text-center">{company} - {location}</small>
      <p className="">{description}</p>
      {image}
    </div>
  )
};
export default JobComponent;