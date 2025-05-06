# Design a File System

## Clarifying Questions
 - I think we're gonna have a file, which will have a name and a createTime right?
 - Each file can be put into a folder?
 - The folders should be able to have sub folders and they should be able to hold files right?
 - Is the system going to support searching for a file or a folder?

## Design Requirements
 - A File class that should be able to handle displaying the file and searching for one
 - A Directory class that should be able to handle displaying the dir and also searching for the dir and searching through all objects in the dir
 - A FileSystem abstract class

 **NOTE**: The problem uses a composite design pattern.