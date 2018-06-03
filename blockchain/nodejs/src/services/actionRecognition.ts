import {environment} from '../environment/environment';
import * as web3 from 'web3';

export class actionRecognition{
private web3:web3;
	private myContractInstance:any
	constructor(){
		this.web3 = new web3();
		this.web3.setProvider(new web3.providers.HttpProvider(environment.nodeURL));

		if (this.web3.isConnected()) { 
			this.myContractInstance = this.web3.eth.contract(environment.contractABI).at(environment.contractAddress);
	        // console.log(`Server connected to ${environment.nodeURL}`);	
	        // console.log(this.web3.fromWei(this.web3.eth.getBalance("0x0Ec793B3F6ECf6FC2D371F7e2000337A1CB47dA6").toNumber(),"ether"));	
	        // console.log("gasprice",this.web3.fromWei(this.web3.eth.gasPrice.toNumber(),"ether") );	
	        // console.log("block",this.web3.eth.getBlock("latest").gasLimit);
	        // console.log("fee",this.web3.fromWei(this.web3.eth.gasPrice.toNumber(),"ether")*this.web3.eth.getBlock("latest").gasLimit);
		} else {
	        let err = new Error("A web3 valid instance must be provided");
	        err.name = "Web3InstanceError";
	        throw err;
		}		
	}	


	public loadClusters():any{
		try{
			let index = this.myContractInstance.totalClusters();
			let clusters = [];
			for(let i=0;i<index;i++){
				clusters.push( this.myContractInstance.loadClusters(i).map((x)=>x*Math.pow(10,-10)) );
			}
			return ({ success:true, data:clusters, error:null });
		}catch(err){
			return ({ success:false, data:null, error:String(err)});
		}		 
	}

	public loadWords():any{
		try{
			let index = this.myContractInstance.totalWords();
			let words = [];
			let f = {};
			for(let i=0;i<index;i++){
				f = {
					name:this.myContractInstance.loadWords(i)[0],
					word:this.myContractInstance.loadWords(i)[1]
				}
				words.push(f);
			}
			return ({ success:true, data:words, error:null });
		}catch(err){
			return ({ success:false, data:null, error:String(err)});
		}		 
	}	


}