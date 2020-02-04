%function 1d2tData() 

% Path access  
desktopPath = fullfile(getenv('HOME'), 'Desktop'); 
transferPath = fullfile(desktopPath, 'Transfer'); 

% Check if transfer directory exist and if not make one
if ~exist(transferPath, 'dir') 
    mkdir(transferPath) 
end 

% Transfer Data from Grid to Local PC
system('scp -r mliza@filexfer.hpc.arizona.edu:/home/u22/mliza/Transfer/* $HOME/Desktop/Transfer');

% Add path to all subfolders 
%addpath(genpath(


%end 
