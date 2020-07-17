---
layout: default
title: Network Infrastructure
parent: Blog
---

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

<div id="greenHeading" markdown="1">
## Environment Setup
{: .fs-7.fw-400 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-0}
</div>

Networking Fundamentals follows a more theory based approach and doesn't involve a lot of practical content. Majority of the practical content that does appear in the following chapter will work regardless of the operating system you are using. However if you would like to be able to follow along exactly with the instructions detailed in this chapter then you should complete the steps in the [OS Setup](#os-setup){:.fs-4 .md-0 .mr-2 }page to replicate the environment that was used by the author.

<div id="greenHeading" markdown="1">
### OS Setup
{: .fs-6 .fw-400 .d-inline-block}
</div>

The exercises in this chapter and their corresponding instructions have been completed on a Linux system. If you already are using Linux then you can move onto the [Application Installation](#application-installation){:.fs-4 .md-0 .mr-0 } section to install the required software.

If you are working on an OS other than Linux I will be detailing two ways to replicate the Linux environment used in this chapter. The first will be using [Docker](#docker-installation-and-setup){:.fs-4 .md-0 .mr-0 } and the second will be using [VirtualBox](#virtualbox-installation-and-setup){:.fs-4 .md-0 .mr-0 }. Both can be downloaded an set up on any major operating system.

<div id="greenHeading" markdown="1">
### Docker or VirtualBox?
{: .fs-6 .fw-400 .d-inline-block}
</div>

Docker will only give you a command line to use and you will have to install the applications that will be used on your own computer. VirtualBox however will give you a Graphical User Interface (GUI) for the operating system you will download. You can install the applications that we will be using on either however for some application we will be using the GUI and so if you are using Docker you will have to download that specific application on your own computer. If you use VirtualBox you can download all the application needed onto the VirtualBox we set up. 

#### Docker Installation and Setup
{: .fs-5 .fw-200 .d-inline-block}

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
<img src="/assets/images/networking/docker1.png">
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
<img src="/assets/images/networking/dockerpullubuntu.png">

Then enter the following:
```shell
docker run -it ubuntu
```
<img src="/assets/images/networking/dockerrunubuntu.png">

You now have a Linux shell running on Ubuntu, if you type:
```shell
ls
```
you will see a list of all the files from the root directory
<img src="/assets/images/networking/ubuntuls.png">

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
<img src="/assets/images/networking/ubuntuexit.png">

We can verify that we have exited the Linux container by looking at the prompt. A prompt in your terminal usually holds information regarding the computer you are on. Information like the current user that is logged in etc. My actual computer prompt you can see from before we ran any of the docker commands. Once we ran the docker container a different looking prompt appeared as we were then inside the Linux container; we had a Ubuntu prompt. After we exited the container the prompt returned to normal. The prompt is the easiest and quickest way to determine if you are still running inside your container or not.

<img src="/assets/images/networking/blurredprompt.png">

You have now created an Ubuntu container using Docker.
{: .d-inline}
</div>

</details >
{: .fs-4 .fw-400 }

#### VirtualBox Installation and Setup
{: .fs-5 .fw-200 .d-inline-block}

Setting up an Linux Virtual Machine (Which is what VirtualBox is allowing us to do) is almost identical on both windows and Mac so the steps below are universal for both operating systems.

<details  id="normalDet" markdown="1">    
<summary>VirtualBox Installation and Set Up [Click]</summary>

1. Go to [Virtual Box Downloads](https://www.virtualbox.org/wiki/Downloads){: .fs-4 .md-0 .mr-0 } click on the platform package that corresponds with your operating system and download VirtualBox
<img src="/assets/images/networking/virtualboxdownload.png">
2. Next head to [Ubuntu Downloads](https://ubuntu.com/download/desktop){:.fs-4 .md-0 .mr-0 } And click download
<img src="/assets/images/networking/ubuntudownload.png">
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

<img src="/assets/images/networking/nameVM.png">
{: .d-block}
</div>

<div markdown="1">
5
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Selecting the memory size. By default it is set to 102MB but I highly recommend you increase the amount of RAM you give to your machine to at lease half of the green portion. Never go into the orange or red areas.
{: .d-inline}

<img src="/assets/images/networking/memsizevm.png">
{: .d-block}
</div>

<div markdown="1">
6
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Creating a Virtual Hard disk. You will need some storage. If you don't have an existing virtual hard disk drive file elsewhere that you wish to use (which most of you wont) then click 'Create a virtual hard disk now'
{: .d-inline}

<img src="/assets/images/networking/createharddiskvm.png">
{: .d-block}
</div>

<div markdown="1">
7
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Choosing a Hard Disk File Type. It will say on the VirtualBox window, but if you do not need this hard disk for other visualization software then you can just leave it as 'VDI (VirtualBox Disk Image)'
{: .d-inline}

<img src="/assets/images/networking/diskfiletypevm.png">
{: .d-block}
</div>

<div markdown="1">
8
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Dynamic or Fixed Size Storage? Choosing dynamic for the word in this chapter is fine since we aren't storing a lot. Since its dynamic if wont immediately take up a fixed amount of memory but rather grow as its needed.
{: .d-inline}

<img src="/assets/images/networking/dynamicvm.png">
{: .d-block}
</div>


<div markdown="1">
9
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; File Location and Size? This is choosing where you are going to store your virtual hard drive which is completely up to you, as well as how big it should be. 10GB is plenty for this chapter.
{: .d-inline}

<img src="/assets/images/networking/filelocationandsizevm.png">
{: .d-block}
</div>


<div markdown="1">
10
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Now select on your VirtualBox in the list on the left hand side of the window then click settings at the top of your window. Once settings has opened click on the 'General' tab at the top of your screen. General has 4 tabs within itself, they are 'Basic', 'Advanced', 'Description' and 'Disk Encryption'. Click on 'Advanced' Copy the settings in the picture below. Then click OK
{: .d-inline}

<img src="/assets/images/networking/clipboardvm.png">
{: .d-block}
</div>

<div markdown="1">
11
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Select  your VirtualBox again from the sidebar and go back into settings. Now head to storage. Your window should look like the picture below. In the 'Storage Devices' list you want to click the first disk that says empty. Like in the picture below. 
After that on the right hand side of the screen click the small blue disk and click the option that says 'Choose Virtual Optical Disk Drive'. A file manager window will open up, navigate to wherever the Ubuntu file you downloaded earlier is. Select the file and click Open.
{: .d-inline}

<img src="/assets/images/networking/storagesettingsvm.png">
<img src="/assets/images/networking/pathtoisovm.png">
{: .d-block}
</div>

<div markdown="1">
12
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; You are now ready to run your virtual machine. Select your machine on the left had side and click run at the top. Once it has loaded you will be prompted with this page. Click 'Install Ubuntu' 
{: .d-inline}

<img src="/assets/images/networking/installubuntuvm.png">
{: .d-block}
</div>

<div markdown="1">
13
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Choose the keyboard layout you wish to use then click continue.
{: .d-inline}

<img src="/assets/images/networking/keyboardlayoutvm.png">
{: .d-block}
</div>

<div markdown="1">
14
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Update and Other Software. You want to select 'Normal Installation' so you get the full features of Ubuntu. Tick 'Download updates while installing Ubuntu' and 'Install third-party software for graphics and Wi-Fi hardware and additional media formats' so that everything is up to date and working.
{: .d-inline}

<img src="/assets/images/networking/updatesandsoftwarevm.png">
{: .d-block}
</div>

<div markdown="1">
15
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Installation Type. You want to select 'Erase disk and install Ubuntu'. Don't worry this wont erase the memory on  your actual, it will be erasing the memory on the virtual hard disk we created which already has nothing on there. 
{: .d-inline}

<img src="/assets/images/networking/installationtypesvm.png">
{: .d-block}
</div>

<div markdown="1">
16
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Where are you? Select you timezone. 
{: .d-inline}

<img src="/assets/images/networking/whereareyouvm.png">
{: .d-block}
</div>

<div markdown="1">
17
{: .fs-3 .d-inline .fw-100 .text-grey-dk-000}

&nbsp; &nbsp; Who are you? This is setting up your user account for this virtual machine.
{: .d-inline}

<img src="/assets/images/networking/whoareyouvm.png">
{: .d-block}

</div>

Thats it your done! Now you have a working Linux VM running on VirtualBox. For the Application Installation Section you can choose to either install software from that section directly onto your computer or onto your VM (granted that the software is compatible with the destination OS). We allocated enough memory for your virtual hard disk drive to store the applications that are mentioned in the installation section.
{: .d-block}

</details>
{: .fs-4 .fw-400 }

<div id="greenHeading" markdown="1">
### Application Installation
{: .fs-6 .fw-400 .d-inline-block}
</div>

Most of the tools that we will be using in the terminal are already installed on Ubuntu. If you already have a distribution of Linux installed that isn't Ubuntu you should still have all the command line tools that are used. However if for some reason you try to use a command line tool in the exercises below and you don't seem to have it on your computer, follow the steps below to install it.

<details  id="normalDet" markdown="1">    
<summary>Application Installation and Set Up [Click]</summary>

1. Open up terminal
2. Type in the following to update your packaging system (System that manages installed packages)
```shell
apt-get update
```
<img src="/assets/images/networking/apt-get-update.png">
3. Then the general form for install a package is
```shell
apt-get install package-name-goes-here
```
In the picture below I've install 'dnsutils' as an example
<img src="/assets/images/networking/apt-get-install.png">

Now you have installed your packet (in my case 'dnsutils')
{: .d-block}

</details>

Wireshark Installation
{: .fs-5 .fw-400}

We will be using Wireshark at different points throughout the chapter. To install:

<details  id="normalDet" markdown="1">    
<summary>Wireshark Installation and Set Up [Click]</summary>

1. Go to [Wireshark Downloads](https://www.wireshark.org/download.html){:.fs-4 .md-0 .mr-0}
2. Click 'Stable Release' and then click the operating system you are using
<img src="/assets/images/networking/wiresharkinstall.png">
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
</details>

</div>

<div  markdown="1">

<div id="yellowHeading" markdown="1">
## Core Knowledge
{: .fs-7.fw-400 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-0}
</div>
<br>

<div id="yellowHeading" markdown="1">
### What Is The Internet? An Introduction!
{: .fs-6 .fw-400 .d-block}
</div>

The Internet is a global network of networks. It is made up from the interconnection of smaller networks, whom may be made up of smaller networks and so on until you create what looks like a tree of networks. The smallest networks in the internet being singular, would be the leaves of your tree. The leaf networks of the internet would be the networks in homes, Small Office Home Office (SOHO) businesses etc.

So what exactly is a network? A network is simply a collection of devices that are connected to each other in some way, which allows them to communicate. So if think about the internet, it is connecting networks of devices with whom could already talk amongst themselves with other devices outside of their network -- specifically with the network they were connected with -- The internet does this with the aim of connecting all networks together. As long as you are connected to some network the internet can connect you to the rest. 
{: .d-block}

<div id="yellowHeading" markdown="1">
#### Overview of the internet
{: .fs-6 .fw-400 .d-block}
</div>

##### What devices make up the Internet?
{: .fs-5 .fw-200 .d-block}

Networks consist of many different types of devices from: Computers, Servers, Smartphones, TVs, Gaming systems etc. When you think about your home network, a leaf on the tree of the internet, can you think of all the devices connected to your internet be it through WIFI or ethernet cable? This would be your Local Area Network (LAN). All the devices that are part of a network are called 'End Systems', or sometimes you will hear 'Hosts'.
{: .d-block}

##### How do devices in the internet connect with each other?
{: .fs-5 .fw-200 .d-block}

End Systems communicate with each other through 'Communication Links' and 'Packet Switches'. There are many different types of communication links that we will go over soon, all you need to know now is that these links are what carry the actual bits of data to and from other end systems. 

When information from one end system wants to travel to another it is not all sent as one big message but rather broken up into smaller packets of information. A packet switch receives packets through a communication link, determines where to send those packets, and then sends them off towards their destination. Their journey will likely involve passing through many packets switches along the way until they arrive at a packet switch that is connected to the destination end system.

This is what is called a 'Packet Switched' network. Another type of network we will be looking at is 'Circuit Switched' networks. We won't get into the details now but the difference in the two surrounds how information gets sent to and from end systems. In a packet switched networks we have learnt that information gets broken up into packets first and then pass through devices that direct them along their path towards their destination. Circuit switched networks however don’t use packets and instead create, big surprise.. Circuits.

There are two common types of packet switches: 
1. Routers
2. Link Layer Switches

The difference between the two lies with how they process the information in packets to determine where to send them. Routers, 'route' packets through the internet, to other routers using the IP address of the destination end system. Each Device connected to the internet has an IP address, something that looks like this:  '157.240.8.35' which is www.facebook.com's IP address for me -- Facebooks IP address will likely be different for you).

<div class="code-example" markdown="1">

To find out the IP address of any website, open up terminal and type the following:

```shell
nslookup website-name-goes-here
```

In the example below we chose www.facebook.com

<img src="/assets/images/networking/nslookupfacebook.png">

</div>

This number is included into every little packet that gets stuffed with information when a end system wants to send something to that IP address. When everyone one of those packets reach a router, the router will examine the IP and then determine which outgoing communication link to send the packet to.

Link Layer Switched however don’t actually look at the IP address at all and instead route those packets using what is called a MAC address. MAC stands for Media Access Control, a MAC address is what allows a Link Layer Switch to uniquely identify a device on the switches network. Since a switch does not use IP addresses it generally isn’t used as much as routers are in the core of the internet since it wont know what to do with incoming packets which have a destination that belongs to a computer outside of the switches network. It only knows about devices that it is physically connected to.

{: .d-block}

##### The Internet provides a service!
{: .fs-5 .fw-200 .d-block}

One reason why the internet has blown up the way it has is because of the service it provides. It allows application on different end systems to be able to communicate with each other. This is why we have electronic mail, Instant Messaging, Online games etc. A application can connect an infinite number of different end systems together to be used for different reasons. Such applications are called distributed application since they are distributed amongst multiple end systems. 

{: .d-block}

#### How do Internet Application Work?
{: .fs-5 .fw-200 .d-block}

Internet Applications define a proprietary protocol or use a public protocol to define how they send and receive information on the internet. A proprietary protocol is one which is designed by a company for use only by that company. A public protocol is defined in what is called a 'Request For Comments' (RFC).

> A Request for Comments (RFC) is a publication from the Internet Society (ISOC) and its associated bodies, most prominently the Internet Engineering Task Force (IETF), the principal technical development and standards-setting bodies for the Internet. 
>...
> An RFC is authored by individuals or groups of engineers and computer scientists in the form of a memorandum describing methods, behaviours, research, or innovations applicable to the working of the Internet and Internet-connected systems. It is submitted either for peer review or to convey new concepts, information, or occasional engineering humor
> -- <cite>Wikipedia</cite>

Public protocols are used by lots of people everywhere in the internet. Applications use protocol that are specific to the sending and receiving data between distributed application over the internet.

{: .d-block}

##### What Are Protocols?
{: .fs-5 .fw-200 .d-block}

Protocols are simply a defined set of instruction with which two entities adhere too to complete some task. In networking, different types of protocols are used for each layer of the internet. We will be going into detail about the different layers of the internet later but what you need to know now is the internet is has 5 different layer and the layers are referred to by the 'Internet layered protocol stack'. Each Layer utilises different protocol to perform their function. 

The top level is the Application layer which looks at the distributed application that use the internet to communicate. The World Wide Web is a Internet application. You use your browser to connect with different servers in the internet that store website data. The way the browser and the servers are able to communicate their needs is through a protocol called HTTP. HTTP provides a language that your browser and some websites server both understand so that you can retrieve the website information to 'surf the web'. HTTP is a public protocol which will be reviewed later, and is just one of many public application protocol defined in a RFC by the IETF. There are also many proprietary application protocol like the protocols Skype uses to connect users all around the world.
{: .d-block}

##### What is the Layered Internet Protocol Stack?
{: .fs-5 .fw-200 .d-block}

The function of the internet is broken up into different layers which together are called the 'Internet Protocol Stack'. The stack has 5 layers, from top to bottom they are:

1. Application Layer
2. Transport Layer
3. Network Layer
4. Link Layer
5. Physical Layer

Each layers is responsible for preforming different tasks, and as we mentioned in the [What are protocols?](#what-are-protocols){:.fs-4 .md-0 .mr-0} section, they perform their function in accordance to specific protocols. This layered architecture of the internet makes it easier to modify and perform maintenance on a specific layer. As you will see soon, each layer:

1. Takes the information from the previous layer below it
2. Does something with that information that will be used by the layer above 
3. Sends that information to the next layer above it.

You can alter the functionality of a layer as long as you still perform the above three steps. The steps ensure that the adjacent layers don’t know the difference of what is happening because the output of the altered layer is the same, however its internal workings may have been improved.

#### Gaining Access To The Internet
{: .fs-6 .fw-400 .d-block}

Gaining access to the internet is a varied process. Ultimately everyone connects through the same steps however at each step there are various different options and choices that each have their advantages and disadvantages. Customers who wish to access the internet can then tailor their connection to their specific needs.
{: .d-block}

Specifically, when you connect the devices in your home to your router, how does that then connect you to the internet. Your routers will use a type of ‘broadband’ internet access to connect you your ‘Internet Service Provider’s’ (ISP) edge router. 
{: .d-block}

##### What is a Modem?
{: .fs-6 .fw-400 .d-block}

When you connect the devices in your home to your router, how does that then connect you to the internet. Your routers will use a type of ‘broadband’ internet access to connect you your ‘Internet Service Provider’s’ (ISP) edge router. 
Most home routers today aren’t just routers, they’re actually 3 different machines compacted into one little box. Those machines are your:
1. Modem
2. Router
3. Wireless Access Point (WAP)
{: .d-block}

You will often hear people use the terms modem and router interchangeable when they are actually very different. This mixup happens so frequently because most of the tasks that your average home user would perform regarding the modem/router/WAP like: plugging it in, restarting it or turning it on, would actually be done to the box that houses all three devices. 

##### Modem
{: .fs-4 .no_toc}

The data that travels along a physical connection to and from the ISP travels in analogue waves, however your computers use digital information.  The modem is responsible for translating that information before your computer receives it so that the computer may understand. Likewise when your computer wants to send information to someone over the internet data needs to leave your computer and travel along some physical mediums, before it does this the modem must convert that digital data back to analogue. 

##### Router
{: .fs-4 .no_toc}

Routers analyse the destination IP addresses of packets passing through that router to determine where to send them next. They use things such as routing tables and protocol to help them better understand the landscape of the internet around them. 

##### Wireless Access Point (WAP)
{: .fs-4 .no_toc}

A Wireless Access Point is a location which allows users to connect to a router through WIFI. Without a wireless access point you would have to be hardwired to a router using a ethernet cable to connect to the internet. (Or use other radio wave based access technologies such as 3g,4g,LTE,5g satellite etc) The Wireless access point then connects to the router using a ethernet cables, so you connect to the WAP through radio waves and the WAP connect you to the router through a ethernet cable. 

##### What Is A ISP?
{: .fs-6 .fw-400 .d-block}

Firstly, what is an ISP? An ISP is a company that provides you access to internet through different forms an packages. In Australia common ISPs are:
1. Telstra
2. Optus
3. Vodafone
{: .d-block}

And the list goes on. They essentially fill the role of connecting different networks together. There are different tiers of ISP which mainly differ in the size of the networks that they connect together.
{: .d-block}
 
Since it is the job of an ISP to connect different networks together, and ISPs are essentially really big networks consisting of lots of smaller networks, ISPs can be connected together by larger ISPs. This is essentially the job of the larger ISPs in the internet, however no matter how big the ISPs are they can always provide access to the smallest network such as a home network. (Generally they don’t since most home networks would be provided access through a smaller ISP.)
{: .d-block}
 
ISPs that refer to a smaller area don’t actually have to be smaller than an ISP that refers to a larger area. E.g. A national ISP for a very small country might consists of fewer networks than a Regional ISP has for a much larger country. However generally the case is that a those smaller ISPs consist of fewer networks. The different types of ISPs approximately from smallest to largest are:
 
##### ‘Local ISPs’
{: .fs-4 .no_toc}

ISPs that provide networks access to customer base in a city or district consisting of homes and corporate customers. They are the smallest type of ISP that there is and are therefore also part of the customer base for bigger ISPs such as Regional, National and International ISPs.
 
##### ‘Regional ISPs’
{: .fs-4 .no_toc}

Similar to local ISPs, a country might even use them interchangeably, however a regional ISP tends to cover a larger area. E.g. A region of a country. They are commonly customers of National, International and Tier 1 ISPs.
 
##### ‘National ISPs’
{: .fs-4 .no_toc}

Generally connect regional ISPs together in a country, are commonly customers of International ISPs and tier 1 ISPs.
 
##### ‘International ISPs’
{: .fs-4 .no_toc}

Generally connect different National ISPs together and therefore provide access to people who want to connect from those different countries. 
{: .d-block}

##### ‘Tier 1 ISPs’
{: .fs-4 .no_toc}

The largest ISPs that exists. There are currently around 13 Tier 1 ISPs and they connect some of the largest networks that exist, forming the global internet. They are not customers of any other ISP other than different Tier 1 ISPs.
{: .d-block}

##### How does a ISP provide me with access to the internet?
{: .fs-6 .fw-400 .d-block}

What are all the different ways an ISP can provide me access to the internet? They are:
 
1. Dial Up
2. Digital Subscriber Line (DSL)
3. Cable
4. Optical Fibre
5. Satellite
6. Cellular

###### Dial up
{: .fs-4}

Dial Up is an older type of internet access that is near extinct due to newer types of access like DSL. Dial Up utilises your telephone line and a dial up modem to connect to the internet. It offers very slow speed with a max of 56Kbps. (For reference the average download speed in the Australia is 40Mbps which is 714x faster.)  Most houses don’t use dial up anymore and instead use DSL, Cable or Optic Fibre.
 
###### Digital Subscriber Line (DSL)
{: .fs-4}

DSL like Dial Up makes use of the existing telephone line you have connected to your house or building. DSL requires that you have a DSL modem as has several improvements on Dial Up most notably that is is much faster and allows you to talk on the phone whilst accessing the internet. To enable this to happen your house will have something called a ‘splitter’ the splitter will divide all incoming signals over a telephone line into signals that are meant to be sent to you DSL modem or signal that are meant to be sent to your telephone.
{: .d-block}

There are different versions of DSL (e.g. ADSL, SDSL, HDSL, VDSL and VDSL2) all which use different frequencies to carry the data as well a telephone data that travels at its own specific frequency. When data leaves your modem and heads to the ISP it reaches a building called a Central Office (CO) which houses the Digital Subscriber Line Access Multiplexer (DSLAM) and a few routers. The DSLAM performs a similar job to the DSL modem, meaning it converts the analogue signals from the communication line into digital form with which can be used by the routers. Likewise it converts incoming data from the routers that are being sent to houses connected to the DSLAM into analogue signals that can travel along the communication lines to a person house, where their modem will turn it back into digital format.

###### Cable
{: .fs-4}

Unlike Dial Up or DSL, Cable doesn’t use telephone wires but instead uses the coaxial cables that provide your house cable TV.  Cable internet also requires an access specific modem, in this case a cable modem.  Cable, like DSL, has to convert between analogue and digital signals for communication link traversal and computer access. It is done in a similar manner to DSL as they have their own system called a Cable Modem Termination System (CMTS) which sits in a building called the cable head end. Cable internet usually incorporates another type of access medium called Optic Fibre. From the cable head end, nodes are connected by optical fibre cables which can handle lots of data with high speeds. These nodes would then spread out into different suburbs and houses would then generally connect to these nodes using coaxial cables. This system is commonly referred to as Hybrid Fibre Coaxial (HFC) 

###### Optical Fibre
{: .fs-4}

Optical Fibre, often called ‘Optic Fibre’ uses a special type of cable to transmit data made of thin glass. Light beams carrying the data bounce from edge to edge within the cable until it reaches its destination. Optic fibre provides very high data speeds since they data is literally moving at the speed of light. This is why Optic Fibre is often used for trans-ocean cables, connecting different countries together. It also provides natural built in defence mechanisms against attacks that rely on tapping into the physical cable to watch or even alter the information that is being passed through it due to the fact that if you try and tap into an Optic Fibre cable it will just break.
{: .d-block}

There are different types of connections such a direct fibre which has an Optic Fibre cable dedicated to each household from the CO. However most ISPs find this to be to expensive with little upside to themselves and rather have fewer cables leaving the CO which split into different paths once they get closer to the destinations.

For the houses that dont use HFC, meaning they have Optic Fibre connecting right to their house, they will have what is called an Optical Network Terminator (ONT). For each home's ONT, there are Optic Fibre cables running to a splitter nearby (similar to the splitter in the DSL however the DSL splitter is just for the house in which it is located in whereas the Optic Fibre splitter is in a area which many houses connect to). The splitter then runs the CO of whatever ISP own thes optic fibre infrastructure and connects to a Optical Line Terminator (OLT) which peroms similar actions to a DSLAM, or a CMTS as it provides conversions between signal used for travelling along physical connection and signals used by computers and routers. However unlike DSLAM and CMTS the OLT converts between Optical signals and Electrical signals.

###### Satellite
{: .fs-4}

Satellite as you might have guessed doesn’t use any physical cables to propagate data from your device to the ISPs but rather satellites. For Satalite internet connection three satelites are used:

1. Attached to your house (Or location where you wish to receive internet)
2. One in space
3. One at the ISP

The satelite in space allows your home satelite to connect from very remote areas as it doesnt rely on existing infrastrcuture like telephone or cable lines. The space satelite can then relay the information it receives to the ISP, which can then send back responses which will pass through the space satelite back to the customer.

The are significant downsides to using satellite such as low internet speeds, high costs and weather interference but they provide a crucial upside that may be the only option to a select group of individuals. Coverage. The main reason you would use satellite is if you’re in such a rural area that you don’t have access to even telephone lines. An example would be on board a container ship in the middle of the ocean. Satellite would be the only real means to access the internet in such a desolate place. 

###### Cellular
{: .fs-4}

Cellular uses whats called the Global System for Mobile communication (GSM) which consists of overlapping base station that can receive radio waves and send them on to other stations to connect you to the internet. Different overallping stations are called cells which is where cellular gets its name.  

Code Division Multiple Access (CDMA) is what allows several different users to send data over the same frequency. It allows this by assigning each transmission a code which uniqeully identifies that transmission, and which can be used to modulate their signal.

To access the GSM users need a Subsriber Identity Module (SIM) card. A SIM card is what uniquelly identified you on the GSM and allowed you to connect to it. 

3G was the first cellular technology that allowed common customers to connect to the internet and so came the advancements to 3G such as Long Term Evolution which could transfer data at higher speeds, then 4G and now even 5G. Unlike WIFI which is also based on radio waves, with cellular you can be kilometres away from a cell tower and yet you will still be able to connect to the internet.  

#### What are the different physical connection types?
Information has to travel to a from end systems by definition if the internet is going it work. So how does this information travel from the router in hour house to the ISP you have purchased you internet subscription from, and then to the rest of the world? We have briefly discussed [different types of internet access available to you](How-does-a-ISP-provide-me-with-access-to-the-internet?) 
and so you already have an idea of the different types of physical connections that are used by ISPs. Each type of connection is different and has the pros and cons, the connections are:

1. Twisted-Pair Copper Wire 
2. Coaxial Cable
3. Fibre Optics
4. Satellite Radio
5. Terrestrial Radio (3g, 4g, LTE, 5g)

###### Twisted-Pair Copper Wire
{: .fs-4}

For Twisted Pair Copper Wire (TP), you have 2 main types: 

1. Shielded (STP)
2. Unshielded (UTP)

The difference between STP and UTP is that for each pari of twisted wires within a cable, STP has a shield that covers those pairs unlike UTP which has the pairs push up close to each other within the cable without a boundary between them. Understandable STP provides more protection against Cross Talk and interference than UTP does.

Both types consist of pairs of twisted copper wire packed together in a cable. They use what’s called Balanced Pair Operation which is a differential mode of transmission simply put, The same signal is sent down both wires that are twisted together to the destination however one of the wires carries the opposite signal. This is done so that once the signals meet its destination the different signals received can be examined and noise from interfering signals can be differentiated from actual data that was being sent over the line. If they wires weren’t twisted and there was interference coming from the right hand side, then whatever cable was on the right would have more interference and so it would be hard to examine and determine what is noise and what is actual signal. 

TP wires also avoid ‘Cross Talk’ which is where cables close together can actually interfere with each other, however twisting a pair together actually insulates that pair from being interfered with by a nearby cable. 

‘Twist Rate’ refers to how tightly twisted the wires are together, the higher the twist rate the less cross talk occurs however also the less distance you receive out of your wires. If you are in an area with very little possible interference, a lower twist rate may be more beneficial as you don’t need as much wire however in a situation with lots of possible sources of interference a higher twist rate and/or Shielded Twisted Pair would be the better option.

For STP specifically, you will also have a ground wire, commonly referred to as a drain wire which ensures to electrical current gets into the copper core. The reason STP has this and UTP doesn’t is because the shielding commonly used in STP is a metal foil which can conduct electricity.

Ethernet Cables are TP cables and there are industry standard on how you arrange the 8 individual wires that are in the ethernet cable into the connector that will inevitable be plugged into your devices. The two standard are T-568A and T-568B. The cables inside the ethernet cables are coloured and some stripped. On the connector you will have letters which tell you which cable goes into which slot in the connector. Upper case letter means it is solid colour cable with a colour that starts with the letter given e.g. G, is solid green cable. BR is solid brown cable. A lower case letter means a white cable with coloured stripes, e.g. br is a white cable with brown stripes, b is a white cable with blue stripes.

###### Coaxial Cable
{: .fs-4}

Coaxial cables are used for cable services. This includes Cable TV and Cable Internet. The coaxial cable itself is build from (Starting from the most inner layer working out):
1. Centre Conductor
2. Dielectric Shield
3. Foil Shield
4. Braided Shield
5. Outer Jacket.

The centre conductor is what carries the actual information transmitted, it is immediately covered by a Dielectric shield which is a plastic insulation that makes sure that no conductivity from the wire leaks out. On top of the plastic insulation there is a foil shield and a braided shield which is meant for protection against interference. 

There are two types of coaxial cable:

1. RG-6
2. RG-59

RG stands for ‘Radio Grade’. RG-6 is generally what will be used for your cable tv. It is more suitable than RG-59 to carry data over longer distances with a higher bandwidth. A big contributor to this increased performance is due to its larger core. The RG-59 is used for shorter distances to perform tasks like analogue video or CCTV. 

Coaxial Cable also has Multiple Channels which is often referred to as ‘Broadband’ in comparison to base band which either uses the whole bandwidth of the cable for data transfer or nothing. Broadband can split the usage of the cable into different frequencies which can send different amounts of data at different times. For Cable internet access over cable tv lines, the digital data is shifted to another frequency as to no interfere with the analogue tv signals. 


###### Optical Fibre
{: .fs-4}

Optic fibre is a very thin and flexible cable that carries light signals. Each pulse of light represents a ‘computer bit’ of information. They are generally made from thin plastic or glass. The light pulses bounce off the walls of the glass until they reach their destination. They allows information to travel a very long distances with very little attenuation.

> > The attenuation is a telecommunication word which refers to reduction within signal strength. This can occur while transmitting signals over lengthy distances. It can be calculated in dB (decibels) in terms of voltage. The function of this is quite opposite to amplification when a signal is transmitted from one place to another place. Once the signal attenuation is extremely high, and then it turns into incoherent. So, most of the networks use repeaters for increasing the signal strength at normal intervals.
>
> -- <cite>https://www.elprocus.com/attenuation-in-optical-fibre-types-and-its-causes/ </cite>
This means Optic fibre requires much fewer repeaters to travel long distances. This characteristic is why it is the ‘go to’ method for physically connecting countries with trans-ocean communication links. 

Optic Fibre is considered a Converged Services which simply means that it can hold many different types of data in a single cable such as:

1. Voice
2. Video
3. Data

The cables itself if comprised of (from most inner components working outwards):

1. Core 
2. Cladding
3. Coating
4. Strength Member
5. Outer Jacket

The core is where the light beams travel through, the coating, strength member and jacket are mainly for protection. However the cladding is important. Cladding can vary in thickness, a thicker cladding produces a softer refraction of the light beams when they bounce off the core walls. Conversely a thinner cladding produces harsher refractions of light that bounce at sharper angles.

Different thickness of cladding are used for different modes of fibre. The two modes are:
1. Single Mode
2. Multimode

Single Mode uses a laser to send the light pulses resulting in a much tighter focus in the ray of light. The single mode is better for sending data across longer distances, this mode is what you would likely see being used in the trans-ocean cables. It doesn’t bounce off the edges anywhere near as much as multimode does and only generally occurs when there are curves in the cables which are natural and are subject to the terrain with which these cables are being placed. 

Multimode uses LEDs to send the light pulses resulting in a less focused beam compared to the single mode fibre. Within multimode fibre you have ‘Single Step’ and ‘Graded Index’, they each describe different fibre core properties which results in outcomes with varying pros and cons for each. Step index was created first and is slower than graded index. Graded index is what is commonly used know to transfer data short distances with a range of a few km’s to and from local ISPs. 

###### Satellite Radio
{: .fs-4}

Satellite Radio as explained in the  [How Does a ISP provide me with access to the internet](How-does-a-ISP-provide-me-with-access-to-the-internet?) uses three satellites to receive and send data through radio waves to and from customers and ISPs. Satellites can communicate with each other in space as well to receive data from one location in the earth and send it to a vastly different location. 

###### Terrestrial Radio (3g, 4g, LTE, and 5g)
{: .fs-4}












</div>

<div id="redHeading" markdown="1">
## Next Step
{: .fs-7.fw-400 .d-inline-block}

Next
{: .fs-2 .fw-200 .label .label-red .px-1 .py-0 .d-inline-block .mt-0}
</div>

<div id="redHeading" markdown="1">
### Practice This Knowledge
{: .fs-6 .fw-400 .d-inline-block}
</div>

<div id="redHeading" markdown="1">
### What To Study Next?
{: .fs-6 .fw-400 .d-inline-block}
</div>
