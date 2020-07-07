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

details {
	border-radius: 2px;
    background: #DEDFF6;
    color: black;
    margin-top: 10px;
    margin-bottom: 15px;


}

details summary {
    font-size: 17px;
    vertical-align: top;
    background: #7F61EF;
    color: #FFF;
    border-radius: 3px;
    padding: 2px 5px;
    outline: none;
    text-align: center;
}

details summary::-webkit-details-marker {
    display: none;
}

details[open] summary:before {
    background-position: -18px 0;
}

details[open] summary {
    background: #6C47EF;
    color: #fff;
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


<details >

<summary> Warning: Instruction May Change! [click]</summary>

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
<details>
<summary> Warning: Unidentified Developer Solution [click]</summary>

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

For Windows Users docker requires some extra steps: follow along here [Docker for Windows](https://docs.docker.com/docker-for-windows/){: .fs-4 .mb-4 .mb-md-0 } or follow the VirtualBox installation of Ubuntu here [VirtualBox](#virtualbox-installation-and-setup){:.fs-4 .md-0 .mr-0 } which may be easier.

{: .d-inline}
</div>

#### VirtualBox Installation and Setup
{: .fs-5 .fw-200 .d-inline-block}

Setup
{: .fs-2 .fw-200 .label .label-green .px-1 .py-0 .d-inline-block .mt-2}

Setting up an Linux Virtual Machine (Which is what VirtualBox is allowing us to do) is almost identical on both windows and Mac so the steps below are universal for both operating systems.

1. Go to [Virtual Box Downloads](https://www.virtualbox.org/wiki/Downloads){: .fs-4 .md-0 .mr-0 } click on the platform package that corresponds with your operating system and download VirtualBox
<img src="https://emmanuelchristianos.github.io//assets/images/networking/virtualboxdownload.png">
2. Next head to [Ubuntu Downloads](https://ubuntu.com/download/desktop){:.fs-4 .md-0 .mr-0 } And click download
<img src="https://emmanuelchristianos.github.io//assets/images/networking/ubuntudownload.png">
3. Open up VirtualBox
<details>
<summary> Warning: Unidentified Developer Solution [click]</summary>

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

Thats it your done! Now you have a working Linux VM running on VirtualBox. For the Application Installation Section you can choose to either install the software from that section directly onto your computer or onto your VM. We allocated enough memory for your virtual hard disk drive to store the applications that are mentioned in the installation section.
{: .d-block}

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
</div>


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

Coming
{: .d-block}

### What Is The Internet? An Introduction!
{: .fs-6 .fw-400 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-1}

Coming
{: .d-block}

#### How Is The Internet Composed?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### What Are Protocols?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### What Is Connecting To The Internet?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### What Devices Facilitate The Functionality Of The Internet?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### There Are Different Types Of Networks?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### Why Is Your Internet Slow Sometimes? How Delay Occurs!
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

#### What Is A Layered Protocol Stack?
{: .fs-5 .fw-200 .d-inline-block}

Core
{: .fs-2 .fw-200 .label .label-yellow .px-1 .py-0 .d-inline-block .mt-2}

Coming
{: .d-block}

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
