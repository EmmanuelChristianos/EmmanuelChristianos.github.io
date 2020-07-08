---
layout: default
title: Network Infrastructure
parent: Blog
---

<style type="text/css">

#warningP {

	margin-left: 10px;
	margin-right: 10px;
	padding-bottom: 10px;
}

#warningD {
	border-radius: 2px;
    background: #DEDFF6;
    color: black;
    margin-top: 10px;
    margin-bottom: 15px;


}

#warningD #warningS {
    font-size: 17px;
    vertical-align: top;
    background: #7F61EF;
    color: #FFF;
    border-radius: 3px;
    border-color: black;
    padding: 2px 5px;
    outline: none;
    text-align: center;
}

#warningD[open] #warningS {
    background: #6C47EF;
    color: #fff;
}

details summary::-webkit-details-marker {
    display: none;
}

details[open] summary:before {
    background-position: -18px 0;
}


#normalDet {

    border: 2px solid #221d7b;
    border-radius: 8px;
    background: #fff;
    color: black;
    margin-top: 10px;
    margin-bottom: 15px;
    padding: 5px;


}


details summary {
    
    font-size: 17px;
    vertical-align: top;
    background: #221d7b;
    color: #fff;
    border-radius: 3px;
    padding: 2px 5px;
    outline: none;
    text-align: center;
}

</style>

# Networking Fundamentals
{: .no_toc .fs-9}

The Network Fundamentals Chapter has a corresponding Github repository which contains the resources used throughout the following chapter.
{: .fs-6 .fw-300 }

[View it on GitHub](https://github.com/EmmanuelChristianos/EmmanuelChristianos.github.io){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}


<div  markdown="1">
## Environment Setup
{: .fs-7.fw-400 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-0}

Networking Fundamentals follows a more theory based approach and doesn't involve a lot of practical content. Majority of the practical content that does appear in the following chapter will work regardless of the operating system you are using. However if you would like to be able to follow along exactly with the instructions detailed in this chapter then you should complete the steps in the [OS Setup](#os-setup){:.fs-4 .md-0 .mr-2 }page to replicate the environment that was used by the author.

{: .d-block}

### OS Setup
{: .fs-6 .fw-400 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-1}

The exercises in this chapter and their corresponding instructions have been completed on a Linux system. If you already are using Linux then you can move onto the [Application Installation](#application-installation){:.fs-4 .md-0 .mr-0 } section to install the required software.

If you are working on an OS other than Linux I will be detailing two ways to replicate the Linux environment used in this chapter. The first will be using [Docker](#docker-installation-and-setup){:.fs-4 .md-0 .mr-0 } and the second will be using [VirtualBox](#virtualbox-installation-and-setup){:.fs-4 .md-0 .mr-0 }. Both can be downloaded an set up on any major operating system.
{: .d-block}


### Docker or VirtualBox?
{: .fs-6 .fw-400 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-1}

Docker will only give you a command line to use and you will have to install the applications that will be used on your own computer. VirtualBox however will give you a Graphical User Interface (GUI) for the operating system you will download. You can install the applications that we will be using on either however for some application we will be using the GUI and so if you are using Docker you will have to download that specific application on your own computer. If you use VirtualBox you can download all the application needed onto the VirtualBox we set up. 
{: .d-block}

#### Docker Installation and Setup
{: .fs-5 .fw-200 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-2}

The following steps will walk you though how to install docker on a mac.
{: .d-block .fs-4}

For Windows Users docker requires some extra steps: follow along here [Docker for Windows](https://docs.docker.com/docker-for-windows/){: .fs-4 .mb-4 .mb-md-0 } or follow the VirtualBox installation of Ubuntu here [VirtualBox](#virtualbox-installation-and-setup){:.fs-4 .md-0 .mr-0 } which may be easier.
{: .d-block .fs-4}


Click below to open up the steps!
{: .d-block .fs-4}

<details  id="normalDet" markdown="1">    
<summary>Docker Installation and Set Up [Click]</summary>

<details id="warningD">
<summary id="warningS"> Warning: Instruction May Change! [Click]</summary>

<p id="warningP">
(Warning: The following instructions might not accurately represent the steps that you need to undertake to install and setup docker.
</p>

<p id="warningP">
Dockers installation and set up process is subject to change by Docker and so the instructions below detail the steps to install and set up Docker at the time of making this chapter.
</p>

<p id="warningP">
It is highly unlikely that the Docker commands themselves will change. However the design on the website will likely change over time.
</p>

<p id="warningP">
If the following steps do not work for you then at the end of the steps there will be a more generalized guide to setting up Docker.)
</p>
</details>
{: .fs-4 .fw-400 }


1. Go to [Docker Website](www.docker.com){: .fs-4 .mb-4 .mb-md-0 } and click on the 'Get Started'
2. Click Docker Desktop 'Download for [Your OS]' (My OS was Mac as you can see in the photo below, yours might be Windows)
<img src="https://emmanuelchristianos.github.io//assets/images/networking/docker1.png">
3. Open the Docker.dmg file and move the docker icon into your application.
4. Go to your applications folder and open Docker

<details id="warningD">
<summary id="warningS"> Warning: Unidentified Developer Solution [click]</summary>

<p id="warningP">
Some Mac users might receive a warning saying 'Docker' can't be opened because it is from  an unidentified developer. If this happens to you follow these steps:
</p>

<p id="warningP">
1. Open up 'Systems Preferences'
</p>

<p id="warningP">
2. Navigate to 'Security & Privacy'
</p>

<p id="warningP">
3. On the menu tab at the top of the system preferences screen click the 'General' tab
</p>

<p id="warningP">
4. At the bottom of the 'General' tab you should see the unidentified developer warning for docker with a button next to it that says 'Open Anyway' click 'Open Anyway'
</p>
</details>
{: .fs-4 .fw-400 }

<div markdown="1">
5
{: .fs-3 .d-inline-block .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; For Mac users open up the application named terminal (this can be found by searching 'terminal' in spotlight)
{: .d-inline}

Enter the following line into the terminal:
```shell
docker pull ubuntu
```
You should have something that looks like this
<img src="https://emmanuelchristianos.github.io//assets/images/networking/dockerpullubuntu.png">

Then enter the following:
```shell
docker run -it ubuntu
```
<img src="https://emmanuelchristianos.github.io//assets/images/networking/dockerrunubuntu.png">

You now have a Linux shell running on Ubuntu, if you type:
```shell
ls
```
you will see a list of all the files from the root directory
<img src="https://emmanuelchristianos.github.io//assets/images/networking/ubuntuls.png">

In the future when the Linux container is needed for an exercise you simply haven to:

1. Open the docker application from your application folder
2. Open up terminal
3. Type the following into terminal:
```shell
docker run -it ubuntu
```
4. Then enter the commands given by the instructions

When you want to exit simply type exit and it will return you to the command line for your actual computer
```shell
exit
```
<img src="https://emmanuelchristianos.github.io//assets/images/networking/ubuntuexit.png">

We can verify that we have exited the Linux container by looking at the prompt. A prompt in your terminal usually holds information regarding the computer you are on. Information like the current user that is logged in etc. My actual computer prompt you can see from before we ran any of the docker commands. Once we ran the docker container a different looking prompt appeared as we were then inside the Linux container; we had a Ubuntu prompt. After we exited the container the prompt returned to normal. The prompt is the easiest and quickest way to determine if you are still running inside your container or not.

<img src="https://emmanuelchristianos.github.io//assets/images/networking/blurredprompt.png">

You have now created an Ubuntu container using Docker.
{: .d-inline}
</div>

</details >
{: .fs-4 .fw-400 }

#### VirtualBox Installation and Setup
{: .fs-5 .fw-200 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-2}

Setting up an Linux Virtual Machine (Which is what VirtualBox is allowing us to do) is almost identical on both windows and Mac so the steps below are universal for both operating systems.

<details  id="normalDet" markdown="1">    
<summary>Docker Installation and Set Up [Click]</summary>

1. Go to [Virtual Box Downloads](https://www.virtualbox.org/wiki/Downloads){: .fs-4 .md-0 .mr-0 } click on the platform package that corresponds with your operating system and download VirtualBox
<img src="https://emmanuelchristianos.github.io//assets/images/networking/virtualboxdownload.png">
2. Next head to [Ubuntu Downloads](https://ubuntu.com/download/desktop){:.fs-4 .md-0 .mr-0 } And click download
<img src="https://emmanuelchristianos.github.io//assets/images/networking/ubuntudownload.png">
3. Open up VirtualBox

<details id="warningD" mardown="1">
<summary id="warningS"> Warning: Unidentified Developer Solution [click]</summary>

<p id="warningP">
Some Mac users might receive a warning saying 'VirtualBox' can't be opened because it is from  an unidentified developer. If this happens to you follow these steps:
</p>

<p id="warningP">
1. Open up 'Systems Preferences'
</p>

<p id="warningP">
2. Navigate to 'Security & Privacy'
</p>

<p id="warningP">
3. On the menu tab at the top of the system preferences screen click the 'General' tab
</p>

<p id="warningP">
4. At the bottom of the 'General' tab you should see the unidentified developer warning for Virtual Box with a button next to it that says 'Open Anyway', click 'Open Anyway'
</p>
</details>
{: .fs-4 .fw-400 }

<div markdown="1">
4
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Once you have opened up VirtualBox, click the blue 'New' button at the top of the screen and you will be prompted with the page below. You want to add a name to the VirtualBox you are creating, select Linux and then select Ubuntu 64 bit. The 'Machine Folder' field is set automatically and you don't need to worry about it.
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/nameVM.png">
{: .d-block}
</div>

<div markdown="1">
5
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Selecting the memory size. By default it is set to 102MB but I highly recommend you increase the amount of RAM you give to your machine to at lease half of the green portion. Never go into the orange or red areas.
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/memsizevm.png">
{: .d-block}
</div>

<div markdown="1">
6
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Creating a Virtual Hard disk. You will need some storage. If you don't have an existing virtual hard disk drive file elsewhere that you wish to use (which most of you wont) then click 'Create a virtual hard disk now'
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/createharddiskvm.png">
{: .d-block}
</div>

<div markdown="1">
7
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Choosing a Hard Disk File Type. It will say on the VirtualBox window, but if you do not need this hard disk for other visualization software then you can just leave it as 'VDI (VirtualBox Disk Image)'
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/diskfiletypevm.png">
{: .d-block}
</div>

<div markdown="1">
8
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Dynamic or Fixed Size Storage? Choosing dynamic for the word in this chapter is fine since we aren't storing a lot. Since its dynamic if wont immediately take up a fixed amount of memory but rather grow as its needed.
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/dynamicvm.png">
{: .d-block}
</div>


<div markdown="1">
9
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; File Location and Size? This is choosing where you are going to store your virtual hard drive which is completely up to you, as well as how big it should be. 10GB is plenty for this chapter.
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/filelocationandsizevm.png">
{: .d-block}
</div>


<div markdown="1">
10
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Now select on your VirtualBox in the list on the left hand side of the window then click settings at the top of your window. Once settings has opened click on the 'General' tab at the top of your screen. General has 4 tabs within itself, they are 'Basic', 'Advanced', 'Description' and 'Disk Encryption'. Click on 'Advanced' Copy the settings in the picture below. Then click OK
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/clipboardvm.png">
{: .d-block}
</div>

<div markdown="1">
11
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Select  your VirtualBox again from the sidebar and go back into settings. Now head to storage. Your window should look like the picture below. In the 'Storage Devices' list you want to click the first disk that says empty. Like in the picture below. 
After that on the right hand side of the screen click the small blue disk and click the option that says 'Choose Virtual Optical Disk Drive'. A file manager window will open up, navigate to wherever the Ubuntu file you downloaded earlier is. Select the file and click Open.
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/storagesettingsvm.png">
<img src="https://emmanuelchristianos.github.io//assets/images/networking/pathtoisovm.png">
{: .d-block}
</div>

<div markdown="1">
12
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; You are now ready to run your virtual machine. Select your machine on the left had side and click run at the top. Once it has loaded you will be prompted with this page. Click 'Install Ubuntu' 
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/installubuntuvm.png">
{: .d-block}
</div>

<div markdown="1">
13
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Choose the keyboard layout you wish to use then click continue.
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/keyboardlayoutvm.png">
{: .d-block}
</div>

<div markdown="1">
14
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Update and Other Software. You want to select 'Normal Installation' so you get the full features of Ubuntu. Tick 'Download updates while installing Ubuntu' and 'Install third-party software for graphics and Wi-Fi hardware and additional media formats' so that everything is up to date and working.
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/updatesandsoftwarevm.png">
{: .d-block}
</div>

<div markdown="1">
15
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Installation Type. You want to select 'Erase disk and install Ubuntu'. Don't worry this wont erase the memory on  your actual, it will be erasing the memory on the virtual hard disk we created which already has nothing on there. 
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/installationtypesvm.png">
{: .d-block}
</div>

<div markdown="1">
16
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Where are you? Select you timezone. 
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/whereareyouvm.png">
{: .d-block}
</div>

<div markdown="1">
17
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Who are you? This is setting up your user account for this virtual machine.
{: .d-inline}

<img src="https://emmanuelchristianos.github.io//assets/images/networking/whoareyouvm.png">
{: .d-block}

</div>

Thats it your done! Now you have a working Linux VM running on VirtualBox. For the Application Installation Section you can choose to either install software from that section directly onto your computer or onto your VM (granted that the software is compatible with the destination OS). We allocated enough memory for your virtual hard disk drive to store the applications that are mentioned in the installation section.
{: .d-block}

</details>
{: .fs-4 .fw-400 }

### Application Installation
{: .fs-6 .fw-400 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-1}

Most of the tools that we will be using in the terminal are already installed on Ubuntu. If you already have a distribution of Linux installed that isn't Ubuntu you should still have all the command line tools that are used. However if for some reason you try to use a command line tool in the exercises below and you don't seem to have it on your computer, follow the steps below to install it.

1. Open up terminal
2. Type in the following to update your packaging system (System that manages installed packages)
```shell
apt-get update
```
<img src="https://emmanuelchristianos.github.io//assets/images/networking/apt-get-update.png">
3. Then the general form for install a package is
```shell
apt-get install package-name-goes-here
```
In the picture below I've install 'dnsutils' as an example
<img src="https://emmanuelchristianos.github.io//assets/images/networking/apt-get-install.png">

Now you have installed your packet (in my case 'dnsutils')
{: .d-block}

Wireshark Installation
{: .fs-5 .fw-400}

We will be using Wireshark at different points throughout the chapter. To install:

1. Go to [Wireshark Downloads](https://www.wireshark.org/download.html){:.fs-4 .md-0 .mr-0}
2. Click 'Stable Release' and then click the operating system you are using
<img src="https://emmanuelchristianos.github.io//assets/images/networking/wiresharkinstall.png">
3. Open it up and your set

<details id="warningD">
<summary id="warningS"> Warning: Unidentified Developer Solution [click]</summary>

<p id="warningP">
Some Mac users might receive a warning saying 'Wireshark' can't be opened because it is from  an unidentified developer. If this happens to you follow these steps:
</p>

<p id="warningP">
1. Open up 'Systems Preferences'
</p>

<p id="warningP">
2. Navigate to 'Security & Privacy'
</p>

<p id="warningP">
3. On the menu tab at the top of the system preferences screen click the 'General' tab
</p>

<p id="warningP">
4. At the bottom of the 'General' tab you should see the unidentified developer warning for Wireshark with a button next to it that says 'Open Anyway', click 'Open Anyway'
</p>
</details>
{: .fs-4 .fw-400 }

<div  markdown="1">
## Prerequisite Knowledge
{: .fs-7.fw-400 .d-inline-block}

Prerequisite
{: .fs-2 .fw-200 .label .label-purple .px-1 .py-0 .d-inline-block .mt-0}

Coming
{: .d-block}
</div>


<div  markdown="1">
## Core Knowledge
{: .fs-7.fw-400 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-0}

### What Is The Internet? An Introduction!
{: .fs-6 .fw-400 .d-block}


#### How Is The Internet Composed?
{: .fs-5 .fw-200 .d-block}

The Internet is a global network of networks. It is made up from the interconnection of smaller networks, whom may be made up of smaller networks and so on until you create what looks like a tree of networks. The smallest networks in the internet being singular, would be the leaves of your tree. The leaf networks of the internet would be the networks in homes, Small Office Home Office (SOHO) businesses etc.

So what exactly is a network? A network is simply a collection of devices that are connected to each other in some way, which allows them to communicate. So if think about the internet, it is connecting networks of devices with whom could already talk amongst themselves with other devices outside of their network -- specifically with the network they were connected with -- The internet does this with the aim of connecting all networks together. As long as you are connected to some network the internet can connect you to the rest. 
{: .d-block}

#### What devices make up the Internet?
{: .fs-5 .fw-200 .d-block}

Networks consist of many different types of devices from: Computers, Servers, Smartphones, TVs, Gaming systems etc. When you think about your home network, a leaf on the tree of the internet, can you think of all the devices connected to your internet be it through WIFI or ethernet cable? This would be your Local Area Network (LAN). All the devices that are part of a network are called 'End Systems', or sometimes you will hear 'Hosts'.
{: .d-block}

#### How do devices in the internet connect with each other?
{: .fs-5 .fw-200 .d-block}

End Systems communicate with each other through 'Communication Links' and 'Packet Switches'. There are many different types of communication links that we will go over soon, all you need to know now is that these links are what carry the actual bits of data to and from other end systems. 

When information from one end system wants to travel to another it is not all sent as one big message but rather broken up into smaller packets of information. A packet switch receives packets through a communication link, determines where to send those packets, and then sends them off towards their destination. Their journey will likely involve passing through many packets switches along the way until they arrive at a packet switch that is connected to the destination end system.

This is what is called a 'Packet Switched' network. Another type of network we will be looking at is 'Circuit Switched' networks. We won't get into the details now but the difference in the two surrounds how information gets sent to and from end systems. In a packet switched networks we have learnt that information gets broken up into packets first and then pass through devices that direct them along their path towards their destination. Circuit switched networks however don’t use packets and instead create, big surprise.. Circuits.

There are two common types of packet switches: 
1. Routers
2. Link Layer Switches

The difference between the two lies with how they process the information in packets to determine where to send them. Routers, 'route' packets through the internet, to other routers using the IP address of the destination end system. Each Device connected to the internet has an IP address, something that looks like this:  '157.240.8.35'  (This is [Facebook's](www.facebook.com){:.fs-4 .md-0 .mr-0} address for me -- Facebooks IP address will likely be different for you) . This number is included into every little packet that gets stuffed with information when a end system wants to send something to that IP address. When everyone one of those packets reach a router, the router will examine the IP and then determine which outgoing communication link to send the packet to.

Link Layer Switched however don’t actually look at the IP address at all and instead route those packets using what is called a MAC address. MAC stands for Media Access Control, a MAC address is what allows a Link Layer Switch to uniquely identify a device on the switches network. Since a switch does not use IP addresses it generally isn’t used as much as routers are in the core of the internet since it wont know what to do with incoming packets which have a destination that belongs to a computer outside of the switches network. It only knows about devices that it is physically connected to.

{: .d-block}

#### The Internet is a service?
{: .fs-5 .fw-200 .d-block}

One reason why the internet has blown up the way it has is because of the service it provides. It allows application on different end systems to be able to communicate with each other. This is why we have electronic mail, Instant Messaging, Online games etc. A application can connect an infinite number of different end systems together to be used for different reasons. Such applications are called distributed application since they are distributed amongst multiple end systems. 

{: .d-block}

#### How do Internet Application Function?
{: .fs-5 .fw-200 .d-block}

Internet Applications define a proprietary protocol or use a public protocol to define how they send and receive information on the internet. A proprietary protocol is one which is designed by a company for use only by that company. A public protocol is defined in what is called a 'Request For Comments' (RFC).

> A Request for Comments (RFC) is a publication from the Internet Society (ISOC) and its associated bodies, most prominently the Internet Engineering Task Force (IETF), the principal technical development and standards-setting bodies for the Internet. 
>...
> An RFC is authored by individuals or groups of engineers and computer scientists in the form of a memorandum describing methods, behaviours, research, or innovations applicable to the working of the Internet and Internet-connected systems. It is submitted either for peer review or to convey new concepts, information, or occasional engineering humor
> -- <cite>Wikipedia</cite>

Public protocols are used by lots of people everywhere in the internet. Applications use protocol that are specific to the sending and receiving data between distributed application over the internet.

{: .d-block}

#### What Are Protocols?
{: .fs-5 .fw-200 .d-block}

Protocols are simply a defined set of instruction with which two entities adhere too to complete some task. In networking different types of protocols are used for each layer of the internet. We will be going into detail about the different layers of the internet later but what you need to know now Is the internet is has 5 different layer and the layers are referred to by the 'Internet layered protocol stack'. Each Layer utilises different protocol to perform their function. 

The top level is the Application layer which looks at the distributed application that use the internet to communicate. The World Wide Web is a Internet application. You use your browser to connect with different servers in the internet that store website data. The way the browser and the servers are able to communicate their needs is through a protocol called HTTP. HTTP provides a language that your browser and some websites server both understand so that you can retrieve the website information to 'surf the web'. HTTP is a public protocol which will be reviewed later, and is just one of many public application protocol defined in a RFC by the IETF. There are also many proprietary application protocol like the protocols Skype uses to connect users all around the world.
{: .d-block}

#### What Is A Layered Protocol Stack?
{: .fs-5 .fw-200 .d-block}

</div>

<div  markdown="1">
## Next Step
{: .fs-7.fw-400 .d-inline-block}

Next
{: .fs-2 .fw-200 .label .label-red .px-1 .py-0 .d-inline-block .mt-0}

Coming
{: .d-block}

### Practice This Knowledge
{: .fs-6 .fw-400 .d-inline-block}

Next
{: .fs-2 .fw-200 .label .label-red .px-1 .py-0 .d-inline-block .mt-1}

Coming
{: .d-block}

### What To Study Next?
{: .fs-6 .fw-400 .d-inline-block}

Next
{: .fs-2 .fw-200 .label .label-red .px-1 .py-0 .d-inline-block .mt-1}

Coming
{: .d-block}

</div>
