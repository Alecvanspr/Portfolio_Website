import React from "react";

const NavButton = ({
    id,
    className="nav-btn",
    label,
}) => {
    return <button id={id} className={className}>{label}</button>
}
export default NavButton;