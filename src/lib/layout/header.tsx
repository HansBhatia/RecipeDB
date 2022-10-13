import { Navbar, Link, Text, Avatar, Button, Input } from "@nextui-org/react";

const Header = () => {
    const collapseItems = [
        "Home",
        "Log Out",
    ];

    return (<>
        <Navbar variant="sticky" css={{ background: '#EB8221 !important' }} containerCss={{ background: '#EB8221 !important' }}>
            <Navbar.Brand >
                {/* ADD LOGO HERE */}
                <Text h3 b color="inherit" hideIn="xs">
                    RecipeDB
                </Text>
            </Navbar.Brand>
            <Navbar.Content hideIn="xs">
                <Navbar.Link css={{ color: "black !important", textDecoration: "underline" }} href="#">Home</Navbar.Link>
            </Navbar.Content>
            <Navbar.Content>
                <Navbar.Link color="inherit" href="#">
                    Login
                </Navbar.Link>
                <Navbar.Link color="inherit" href="#">
                    Sign Up
                </Navbar.Link>
            </Navbar.Content>
        </Navbar></>)
}

export default Header;